import datetime
from safarisapp.models import Current_user_booking


def find_duration(Booking_from, Booking_to):
    booking_duration = []
    start  = Current_user_booking.objects.order_by('Booking_from')[-1].get()
    end = Current_user_booking.objects.order_by('Booking_to')[-1].get()
    
    booking_duration.append(start, end)
    