from safarisapp.Booking.apartments_booking import check_room_availability
from django import forms
from django.http import request
from django.http.response import HttpResponse
from umarsafaris.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Carfeatures, Apartmentsbase,  Contact, Current_user_booking, Ourteam, SendMessage
from .forms import Client_Booking_ApartmentForm, aptbookingForm
#from safarisapp.Booking.apartments_booking import check_room_availability
from django.utils.html import strip_tags
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
        form = aptbookingForm(request.POST)
        
        if form.is_valid():
            Apartments_Available = form.cleaned_data.get('Apartments_Available')
            Name = form.cleaned_data.get('Name')
            Email = form.cleaned_data.get('Email')
            ID_No = form.cleaned_data.get('ID_No')
            Tel = form.cleaned_data.get('Tel')
            date_in = form.cleaned_data.get('Check_In')
            date_out = form.cleaned_data.get('Check_Out')
            
            room_list = Client_Booking_ApartmentForm.objects.filter(Apartments_Available='Apartments_Available')
            room_available = []
            
            for rooms in room_list:
                if check_room_availability(Apartments_Available, date_in, date_out):
                    room_available.append(rooms)
                    
                    form.save()
                    
                else:
                    return HttpResponse('The room has been booked for the period you entered. Please select another one')
            
            
            
            
            #form.save()
            #send mail to the client on booking details
            
            title = "Thank you for booking with UmarSafaris. Here is Your Booking Details"
            
            message1 = str( date_in)
            message2 = str( date_out)
            msg_list = [Name, Apartments_Available, Email, ID_No, Tel, message1, message2]
            message = str(msg_list)
            
            send_mail(
                title,
                message,
                settings.EMAIL_HOST_USER,
                [Email]
            )
            
            messages.success(request, f'{Name} thank you for booking with UmarSafaris,\n You have booked Apartment {Apartments_Available}\n Available from {date_in} to {date_out} \\n You will Receive an Email shortly containing your booking infomation. If you don\'t receive any email within the next 10mins please reach our support team. Other Details\n Phone Number:{Tel}\n ID_No\Passport No:{ID_No}')
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