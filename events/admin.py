from django.contrib import admin
from django.utils.html import format_html
from .models import EventCategory, EventService, Booking, ContactMessage


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(EventService)
class EventServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price_start')
    list_filter = ('category',)
    search_fields = ('title', 'category__name')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'service', 'event_date', 'status_colored', 'created_at')
    list_filter = ('status', 'event_date', 'service__category')
    search_fields = ('customer_name', 'phone', 'service__title', 'service__category__name')
    date_hierarchy = 'event_date'
    ordering = ('-created_at',)

    def status_colored(self, obj):
        color = {
            'pending': 'orange',
            'confirmed': 'limegreen',
            'cancelled': 'crimson'
        }.get(obj.status, 'gray')
        return format_html(
            '<span style="color:{}; font-weight:600; text-transform:capitalize;">{}</span>',
            color,
            obj.get_status_display()
        )

    status_colored.short_description = 'Status'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_at')
    search_fields = ('name', 'subject', 'email')
