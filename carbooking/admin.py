from django.contrib import admin
from carbooking.models import Cars_Available, Current_caruser_booking

# Register your models here.
class Cars_AvailableAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'milage', 'image')
    search_fields = ('name', 'model')
    prepopulated_fields = {"slug": ("name",)}


class Current_caruser_bookingAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Second_Name', 'ID_No', 'carpicked', 'Email', 'Contact' )
    search_fields = ('Email', 'Contact', 'Second_Name', 'ID_No',)


admin.site.register(Cars_Available, Cars_AvailableAdmin),
admin.site.register(Current_caruser_booking, Current_caruser_bookingAdmin),