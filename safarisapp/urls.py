from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('testimonial/', TestimonialListView.as_view(), name='testimonial'),
    path('about/', AboutListView.as_view(), name='about'),
    path('', ImageInHomeListView.as_view(), name='homephoto')
    
]