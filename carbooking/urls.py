from django.urls import path
from . import views
from .views import check_valid_data, CarspageListView, CarDetailView

urlpatterns = [
    path('car_booking_details', views.car_booking_details, name='car_booking_details'),
    path('cars/booking/', views.check_valid_data, name='user-booking'),
    path('cars/', CarspageListView.as_view(), name='car'),
    path('cars/<slug:slug>', CarDetailView.as_view(), name='car-detail'),
    
]