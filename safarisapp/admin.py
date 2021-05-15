from django.contrib import admin
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
    
class Current_user_bookingAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Second_Name', 'ID_No', 'carpicked', 'Email', 'Contact' )
    list_filter = ('ID_No', 'carpicked', 'Email',)
    search_fields = ('Email', 'Contact', 'Second_Name', 'ID_No',)
    
    
admin.site.register(Apartmentsbase, ApartmentsbaseAdmin),
admin.site.register(Carfeatures, CarfeaturesAdmin),
admin.site.register(Contact, ContactAdmin)
admin.site.register(Current_user_booking, Current_user_bookingAdmin),
admin.site.register(SliderImage)
admin.site.register(About)

