from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories_list, name='categories'),
    path('category/<int:category_id>/services/', views.services_by_category, name='services_by_category'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('service/<int:service_id>/book/', views.book_service, name='book_service'),
    path('booking/<int:booking_id>/success/', views.booking_success, name='booking_success'),
    path('gallery/', views.gallery, name='gallery'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
