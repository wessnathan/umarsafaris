from django.db import models
from carbooking.models import Cars_Available, Current_caruser_booking
import datetime


def find_car_choice_id(carpicked):
    car_list = Cars_Available.objects.filter(name=carpicked).values_list('id', 'name', 'model')
    
    car_choice_id = car_list[0][0]
    
    return car_choice_id


def is_car_available_now(car_id, Check_In, Check_Out):
    car_users_dict  = Current_caruser_booking.objects.filter(carpicked=car_id).exclude(Check_Out=datetime.date.today()).values('Check_In','Check_Out')
    
    for bookings in car_users_dict:
        if bookings.get('Check_In',0) < Check_In <bookings.get('Check_Out',0) or bookings.get('Check_Out', 0) >Check_Out:
            
            return False
        else:
        
            return True