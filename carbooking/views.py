from carbooking.car_booking.check_available_car import find_car_choice_id, is_car_available_now
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import DetailView
#from django.views.decorators.csrf import crsf_exempt
from django.http.response import HttpResponse, JsonResponse
#from django rest_framework.parsers import JSONParser
from umarsafaris.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib import messages
from django.conf import settings
from carbooking.models import Cars_Available, Current_caruser_booking
from carbooking.forms import Car_BookingForm
from carbooking.serializers import Current_caruser_bookingSerializer
from django.views.decorators.csrf import csrf_exempt
#from rest_framework import JSONParser
from django.views.decorators import csrf
#from rest_framework.serializers import Serializer


def car_booking_details(request):
    return render(request, 'forms/car_thanks.html')


def check_valid_data(request):
    if request.method == "POST":
        form = Car_BookingForm(request.POST)
        
        if form.is_valid():
            First_Name = form.cleaned_data.get('First_Name')
            Second_Name = form.cleaned_data.get('Second_Name')
            carpicked = form.cleaned_data.get('carpicked')
            ID_No = form.cleaned_data.get('ID_No')
            Email = form.cleaned_data.get('Email')
            Contact = form.cleaned_data.get('Contact')
            Check_In = form.cleaned_data.get('Check_In')
            Check_In_Time = form.cleaned_data.get('Check_In_Time')
            Check_Out = form.cleaned_data.get('Check_Out')
            Check_Out_Time = form.cleaned_data.get('Check_Out_Time')
            
            form.save(commit=False)
            
            selected_car = find_car_choice_id(carpicked)
            print(selected_car, Check_In, Check_Out, carpicked)
            
            car_status = is_car_available_now(selected_car, Check_In, Check_Out)
            print(car_status)
            
            if car_status == True or car_status == None:
                
                form.save()
                
                date_in = str(Check_In)
                time_in_n = str(Check_In_Time)
                date_out = str(Check_Out)
                time_out_n = str(Check_Out_Time)
                
                print(time_in_n, time_out_n)
                
                #email template to send email to user
                
                template_name = 'email_templates/email_template.html'  #get_template('email_template.html')
                
                context_data =  {'First_Name':First_Name, 'Second_Name':Second_Name, 'ID_No':ID_No, 
                                                                                'Email':Email, 'Contact':Contact, 'Check_In':Check_In, 'Check_In_Time':Check_In_Time,
                                                                                    'Check_Out':Check_Out, 'Check_Out_Time':Check_Out_Time, 'carpicked':carpicked }
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
                messages.success(request, f'{First_Name}{Second_Name} thank you for booking with UmarSafaris, You have Rented {carpicked} Available from {date_in}{time_in_n} to {date_out}{time_out_n} You will Receive an Email shortly containing your booking infomation. If you don\'t receive any email within the next 10mins please reach our support team. Other Details: Email:{Email} Phone Number:{Contact} ID_No\Passport No:{ID_No}')
                return redirect('car_booking_details')
            
            else:
                messages.warning(request, f' {First_Name} {Second_Name}, {carpicked} has been rented for that particular period. Please select another one .Thank you')
                return redirect('user-booking')
        
    else:
        form = Car_BookingForm()
        
    return render(request, 
                    'forms/car_booking_form.html',
                    {
                        'form':form
                        }
                    )
    

class CarspageListView(ListView):
    model = Cars_Available
    template_name = 'carbooking/cars_available_list.html'
    context_object_name = 'carpage'
    
    
class CarDetailView(DetailView):
    model = Cars_Available
    template_name = 'carbooking/cars_available_detail.html'
    

#@crsf_exempt
#def booked_user_list(request):
    
    #if request.method == 'GET':
        #booked_user = Current_caruser_booking.objects.all()
        #serializer = Current_caruser_bookingSerializer(booked_user, many=True)
        #return JsonResponse(serializer.data, safe=False)
    #elif request.method == 'POST':
        #data = JSONParser().parse(request)
        #serializer = Current_caruser_bookingSerializer(data=data)
        
        #if serializer.is_valid():
            #serializer.save()
            #return JsonResponse(serializer.data, status=201)
        #return JsonResponse(serializer.errors, status=400)
        
        
        
        
        
        
        
        
        
        