from django.shortcuts import render, get_object_or_404, redirect
from .models import EventCategory, EventService, Booking
from .forms import BookingForm, ContactForm
from django.contrib import messages

def home(request):
    categories = EventCategory.objects.all()
    featured_services = EventService.objects.all()[:6]
    return render(request, 'events/home.html', {
        'categories': categories,
        'featured_services': featured_services
    })


def categories_list(request):
    categories = EventCategory.objects.all()
    return render(request, 'events/categories.html', {'categories': categories})


def services_by_category(request, category_id):
    category = get_object_or_404(EventCategory, id=category_id)
    services = category.services.all()
    return render(request, 'events/services.html', {
        'category': category,
        'services': services
    })


def service_detail(request, service_id):
    service = get_object_or_404(EventService, id=service_id)
    return render(request, 'events/service_detail.html', {'service': service})



def book_service(request, service_id):
    service = get_object_or_404(EventService, id=service_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service = service
            booking.save()
           # messages.success(request, "Your booking request has been submitted successfully!")
            return redirect('booking_success', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'events/booking.html', {
        'service': service,
        'form': form
    })
def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'events/booking_success.html', {
        'booking': booking
    })

def about(request):
    return render(request, 'events/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us. We will get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'events/contact.html', {'form': form})

def gallery(request):
    # only services that have an image
    services_with_images = EventService.objects.exclude(image='').exclude(image__isnull=True)
    return render(request, 'events/gallery.html', {
        'services': services_with_images
    })
