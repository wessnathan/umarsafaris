from django.db import models
from django.http.response import HttpResponse
from umarsafaris.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic.list import ListView
from safarisapp.models import Contact, Ourteam, SendMessage, ImagesOnHome


def home(request):
    return render(request, 'safarisapp/index.html')


def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        title = request.POST['title']
        tel = request.POST['tel']
        message = request.POST['message']
        
        #mail sending
        send_mail(
            title,#subject
            message ,#message
            email,#from 
            ['umarsafariskenya@gmail.com', 'kelvinumar@yahoo.com'],#to
        )
        save_inquiry_info = Contact(fname=fname, email=email, tel=tel, message=message, title=title)
        save_inquiry_info.save()
        
        return render(request, 'safarisapp/contact.html', {'fname':fname})
    else:
        
        return render(request, 'safarisapp/contact.html')


class TestimonialListView(ListView):
    model = SendMessage
    template_name = 'safarisapp/sendmessage_list.html'
    context_object_name = 'msg'


class AboutListView(ListView):
    model = Ourteam
    template_name = 'safarisapp/ourteam_list.html'
    context_object_name = 'team'


class ImageInHomeListView(ListView):
    models = ImagesOnHome
    template_name = 'safarisapp/index.html'
    context_object_name = 'homephoto'

