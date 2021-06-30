from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import *



class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'title', 'tel', 'email', 'date')
    search_fields = ('fname', 'tel', 'email', 'date')


class SendMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'dt')
    search_fields = ('email', 'dt')


class OurteamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('position', 'email')
    
    

admin.site.register(Contact, ContactAdmin)
admin.site.register(About)
admin.site.register(SendMessage)
admin.site.register(Ourteam)
admin.site.register(ImagesOnHome)

