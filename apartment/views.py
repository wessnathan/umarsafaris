from django.shortcuts import render, redirect
from django.http import request
from django.http.response import HttpResponse
from umarsafaris.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from apartment.models import Umarsafarisrooms
from .forms import User_BookingForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



def booking_details(request):
    return render(request, 'forms/thanks.html')


def  booking_apartments(request):
    
    if request.method == 'POST':
        form = User_BookingForm(request.POST)
        
        if form.is_valid():
            Rooms = form.cleaned_data.get('Rooms')
            Name = form.cleaned_data.get('Name')
            Email = form.cleaned_data.get('Email')
            ID_No = form.cleaned_data.get('ID_No')
            Tel = form.cleaned_data.get('Tel')
            date_in = form.cleaned_data.get('Check_In')
            time_in = form.cleaned_data.get('Check_In_Time')
            date_out = form.cleaned_data.get('Check_Out')
            time_out = form.cleaned_data.get('Check_Out_Time')
            
            
            
            form.save()
            #send mail to the client on booking details
            
            title = "Thank you for booking with UmarSafaris. Here is Your Booking Details"
            
            message1 = str( date_in)
            message2 = str( date_out)
            time_in_n =str(time_in)
            time_out_n =str(time_out)
            msg_list = [Name, Rooms, Email, ID_No, Tel, message1,time_in_n, message2, time_out_n]
            message = str(msg_list)
            
            send_mail(
                title,
                message,
                settings.EMAIL_HOST_USER,
                [Email]
            )
            
            messages.success(request, f'{Name} thank you for booking with UmarSafaris, You have booked Apartment {Rooms} Available from {date_in}{time_in_n} to {date_out}{time_out_n} You will Receive an Email shortly containing your booking infomation. If you don\'t receive any email within the next 10mins please reach our support team. Other Details\n Phone Number:{Tel}\n ID_No\Passport No:{ID_No}')
            return redirect('client_booking_details')
    else:
        form = User_BookingForm()
    return render(request,
                    "forms/apartment_booking_form.html",
                    {
                        'form':form
                        }
                    )
        

class ApartmentsListView(ListView):
    model = Umarsafarisrooms
    template_name = 'apartment/apartmentbase_list.html'
    context_object_name = 'aptno'


class ApartmentsDetailView(DetailView):
    model = Umarsafarisrooms
    template_name = 'apartment/apartmentsbase_detail.html'
    
    
