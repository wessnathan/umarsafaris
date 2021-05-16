from django.shortcuts import render, redirect
from django.core.mail import send_mail
#from django.contrib import messages
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Carfeatures, Apartmentsbase, Contact, Current_user_booking, SendMessage


def home(request):
    return render(request, 'safarisapp/index.html')

def about(request):
    return render(request, 'safarisapp/about.html')

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
        return render(request, 'safarisapp/carfeatures_detail.html', {'First_Name':First_Name, 'Second_Name':Second_Name, 'ID_No':ID_No, 
                                                                        'Email':Email, 'Contact':Contact, 'Booking_from':Booking_from,
                                                                            'Booking_to':Booking_to, 'carpicked':carpicked })
    else:
        return render(request, 'safarisapp/carfeatures_detail.html' )

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

    
class CarDetailView(DetailView):
    model = Carfeatures
    template_name = 'safarisapp/carfeatures_detail.html'
    
    
class ApartmentsDetailView(DetailView):
    model = Apartmentsbase
    template_name = 'safarisapp/apartmentsbase_detail.html'