from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.check_valid_data, name='user-booking'),
    path('cars/', CarspageListView.as_view(), name='car'),
    path('apartment/', ApartmentsListView.as_view(), name='apartments'),
    path('testimonial/', TestimonialListView.as_view(), name='testimonial'),
    path('about/', AboutListView.as_view(), name='about'),
    path('cars/<slug:slug>', CarDetailView.as_view(), name='car-detail'),
    path('apartments/<slug:slug>', ApartmentsDetailView.as_view(), name='apartment-detail'),
    
]