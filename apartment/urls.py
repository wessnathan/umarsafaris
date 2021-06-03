from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('apartments/client_booking_details', views.booking_details, name='client_booking_details'),
    path('apartments/booking-apartments', views.booking_apartments, name='book-apt'),
    path('apartments/', ApartmentsListView.as_view(), name='apartments'),
    path('apartments/<slug:slug>', ApartmentsDetailView.as_view(), name='apartment-detail'),
    
]