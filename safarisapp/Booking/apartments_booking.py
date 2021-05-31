import datetime
from safarisapp.forms import Client_Booking_ApartmentForm

def check_room_availability(Apartments_Available, date_in, date_out):
    Apartment_not_booked =[]
    booking_list = Client_Booking_ApartmentForm.objects.filter(Apartments_Available='Apartments_Available')
    
    for booking in booking_list:
        if booking.Check_In >date_out or booking.Check_Out <date_in:
            Apartment_not_booked.append(True)
            
        else:
            Apartment_not_booked.append(False)
            
    return all(Apartment_not_booked)
    