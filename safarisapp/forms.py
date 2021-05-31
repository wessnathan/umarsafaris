from safarisapp.models import Apartmentsbase
from django.db import models
from django import forms
from django.db.models.deletion import CASCADE
from django.forms import widgets
import datetime




class Client_Booking_ApartmentForm(models.Model):
    
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Room = models.ForeignKey(Apartmentsbase, on_delete=models.CASCADE)
    ID_No = models.CharField(max_length=30)
    Tel =models.CharField(max_length=13)
    Check_In = models.DateTimeField()
    Check_Out = models.DateTimeField()
    
    
    def __str__(self):
        return f'{self.Name} has Booked Apartment {self.Apartments_Available} from{self.Check_In} to {self.Check_Out}, {self.Email}, {self.Tel}, {self.ID_No}'
        
    class Meta:
        verbose_name_plural = " Apartments Booked By Clients"
        
        

class aptbookingForm(forms.ModelForm):
    
    Apartment_Choices = (
        ('DEL', (('DL1', 'D1'),('DL2', 'D2'))),
        ('Rook', 'RK1'),
        ('Bishop', 'BP1'),
        ('Castle', 'CST1'),
    )
    
    Apartments_Available = forms.ChoiceField(choices=Apartment_Choices, required=True)
    
    class Meta:
        model = Client_Booking_ApartmentForm
        fields = '__all__'
        exclude = ['Room']
        widgets = {
            'Check_In':widgets.SelectDateWidget(
                                    empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                    ),
            'Check_Out':widgets.SelectDateWidget(
                                    empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                    )
        }
        
        