from django.db import models

# Create your models here.

class EventCategory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Event Categories"

    def __str__(self):
        return self.name


class EventService(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=250)
    price_start = models.DecimalField(max_digits=10, decimal_places=2, help_text="Starting price")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    short_description = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    service = models.ForeignKey(EventService, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    event_date = models.DateField()
    event_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=250)
    guests_count = models.PositiveIntegerField(blank=True, null=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.customer_name} - {self.service.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
