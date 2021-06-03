from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import *



class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'title', 'tel', 'email', 'date')
    list_filter = ('fname', 'email')
    search_fields = ('fname', 'tel', 'email', 'date')


class SendMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'dt')
    list_filter = ('email')
    search_fields = ('email', 'dt')


class OurteamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_filter = ('position')
    search_fields = ('position', 'email')
    
    

admin.site.register(Contact, ContactAdmin)
admin.site.register(About)
admin.site.register(SendMessage)
admin.site.register(Ourteam)

