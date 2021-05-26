from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .forms import Client_Booking_ApartmentForm
from .models import *

class CarfeaturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'milage', 'image')
    list_filter = ('model', 'publish')
    search_fields = ('name', 'model')
    prepopulated_fields = {"slug": ("name",)}
    
class ApartmentsbaseAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Rooms',)
    list_filter = ('Name', 'Rooms')
    search_fields = ('Name', 'Rooms')
    prepopulated_fields = {"slug": ("Name",)}
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'title', 'tel', 'email', 'date')
    list_filter = ('fname', 'email')
    search_fields = ('fname', 'tel', 'email', 'date')
    
class Client_Booking_ApartmentFormAdmin(admin.ModelAdmin):
    list_display = ('Name', 'ID_No', 'Email', 'Tel')
    list_filter = ('Name', 'ID_No')
    search_fields = ('Name', 'ID_No', 'Email', 'Tel', 'Check_In', 'Check_Out')
    
class Current_user_bookingAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Second_Name', 'ID_No', 'carpicked', 'Email', 'Contact' )
    list_filter = ('ID_No', 'carpicked', 'Email',)
    search_fields = ('Email', 'Contact', 'Second_Name', 'ID_No',)
    
class SendMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'dt')
    list_filter = ('email')
    search_fields = ('email', 'dt')
    
class OurteamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_filter = ('position')
    search_fields = ('position', 'email')
    
    
admin.site.register(Apartmentsbase, ApartmentsbaseAdmin),
admin.site.register(Carfeatures, CarfeaturesAdmin),
admin.site.register(Contact, ContactAdmin)
admin.site.register(Current_user_booking, Current_user_bookingAdmin),
admin.site.register(Client_Booking_ApartmentForm, Client_Booking_ApartmentFormAdmin)
admin.site.register(SliderImage)
admin.site.register(About)
admin.site.register(SendMessage)
admin.site.register(Ourteam)

