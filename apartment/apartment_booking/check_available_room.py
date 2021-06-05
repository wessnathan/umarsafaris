from apartment.models import Booking_ApartmentsForm, Umarsafarisrooms
import datetime



def find_choice_id(Apartment):
    rooms_list = Umarsafarisrooms.objects.filter(Name=Apartment).values_list('id', 'Rooms', 'Name')
    
    choice_id = rooms_list[0][0]
    
    return choice_id
    
    
def check_if_room_is_available(room_id, date_in, date_out):
    booking_dict = Booking_ApartmentsForm.objects.filter(Apartment=room_id).exclude(Check_Out__lt=datetime.date.today()).values('Check_In','Check_Out')
    
    for bookings in booking_dict:
        if bookings.get('Check_In',0) < date_in <bookings.get('Check_Out',0) or bookings.get('Check_Out', 0) >date_out:
            
            return False
        else:
        
            return True
        
        