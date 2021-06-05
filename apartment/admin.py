from django.contrib import admin
from apartment.models import Umarsafarisrooms, Booking_ApartmentsForm

# Register your models here.
class UmarsafarisroomsAdmin(admin.ModelAdmin):
    list_display = ( 'Name','Beds',)
    list_filter = ('Name', 'Beds',)
    search_fields = ('Name', 'Beds',)
    prepopulated_fields = {"slug": ("Name",)}
    
    
class Booking_ApartmentsFormAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Apartment', 'Email', 'Tel', 'Check_In', 'Check_In_Time', 'Check_Out', 'Check_Out_Time')
    list_filter = ('ID_No', 'Email',)
    search_fields = ('Name', 'ID_No', 'Email', 'Tel','Rooms', 'Check_In', 'Check_In_Time', 'Check_Out', 'Check_Out_Time')


admin.site.register(Umarsafarisrooms, UmarsafarisroomsAdmin)
admin.site.register(Booking_ApartmentsForm, Booking_ApartmentsFormAdmin)