from django import forms
from django.http import request
from umarsafaris.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.html import strip_tags
from django.conf import settings
#from django.contrib import messages
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Carfeatures, Apartmentsbase,  Contact, Current_user_booking, Ourteam, SendMessage
from .forms import aptbookingForm
import datetime


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
    
    
def check_valid_data(request):
    if request.method == "POST":
        First_Name = request.POST['First_Name']
        Second_Name = request.POST['Second_Name']
        carpicked = request.POST['cars-available']
        ID_No = request.POST['ID_No']
        Email = request.POST['Email']
        Contact = request.POST['Contact']
        Booking_from = request.POST['Booking_from']
        Booking_to = request.POST['Booking_to']
        
        
        booking_info = Current_user_booking(First_Name=First_Name, Second_Name=Second_Name,
                                            ID_No=ID_No, Email=Email,
                                            Contact=Contact, Booking_from=Booking_from,
                                            Booking_to=Booking_to, carpicked=carpicked)
        
        booking_info.save()
        
        #started
        
        template_name = 'email_templates/email_template.html'  #get_template('email_template.html')
        
        context_data =  {'First_Name':First_Name, 'Second_Name':Second_Name, 'ID_No':ID_No, 
                                                                        'Email':Email, 'Contact':Contact, 'Booking_from':Booking_from,
                                                                            'Booking_to':Booking_to, 'carpicked':carpicked }
        email_html_template = get_template(template_name).render(context_data)
        
        
        email = EmailMultiAlternatives(
            #subject
            "Thank you For Booking at UmarSafaris ",
            #content
            email_html_template,
            #from
            settings.EMAIL_HOST_USER,
            #to
            [Email]
            
        )
        
        email.attach_alternative(email_html_template, 'text/html')
        email.send()
        
        return render(request, 'safarisapp/carfeatures_detail.html', {'First_Name':First_Name, 'Second_Name':Second_Name, 'ID_No':ID_No, 
                                                                        'Email':Email, 'Contact':Contact, 'Booking_from':Booking_from,
                                                                            'Booking_to':Booking_to, 'carpicked':carpicked })
        
        
    else:
        return render(request, 'safarisapp/carfeatures_detail.html' )
    
    
def booking_details(request):
    return render(request, 'forms/thanks.html')


def  booking_apartments(request):
    
    if request.method == 'POST':
        todays_date = datetime.date.today()
        form = aptbookingForm(request.POST, initial={'Check_In':todays_date})
        
        if form.is_valid:
            
            
            form.save()
            
            return redirect('client_booking_details')
    else:
        form = aptbookingForm()
    return render(request, 'forms/apartment_booking_form.html', {'form':form})
        

class CarspageListView(ListView):
    model = Carfeatures
    template_name = 'safarisapp/carfeatures_list.html'
    context_object_name = 'carpage'
    
    
class ApartmentsListView(ListView):
    model = Apartmentsbase
    template_name = 'safarisapp/apartmentbase_list.html'
    context_object_name = 'aptno'
    
    
class TestimonialListView(ListView):
    model = SendMessage
    template_name = 'safarisapp/sendmessage_list.html'
    context_object_name = 'msg'
    
    
class AboutListView(ListView):
    model = Ourteam
    template_name = 'safarisapp/ourteam_list.html'
    context_object_name = 'team'

    
class CarDetailView(DetailView):
    model = Carfeatures
    template_name = 'safarisapp/carfeatures_detail.html'
    
    
class ApartmentsDetailView(DetailView):
    model = Apartmentsbase
    template_name = 'safarisapp/apartmentsbase_detail.html'