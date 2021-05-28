from django.db import models
from django import forms
from django.forms import widgets
import datetime



class Client_Booking_ApartmentForm(models.Model):
    Apartment_Choices = (
        ('DEL', 'DL1'),
        ('Rook', 'RK1'),
        ('Bishop', 'BP1'),
        ('Castle', 'CT1'),
    )
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Apartments_Available = models.CharField(max_length=10, choices=Apartment_Choices, default='Available')
    ID_No = models.CharField(max_length=30)
    Tel =models.PositiveIntegerField()
    Check_In = models.DateTimeField()
    Check_Out = models.DateTimeField()
    
    
    def __str__(self):
        return f'{self.Name} has Booked Apartment from{self.Check_In} to {self.Check_Out}, {self.Email}, {self.Tel}, {self.ID_No}'
        
    class Meta:
        verbose_name_plural = "Booked Apartments By Clients"
        
        

class aptbookingForm(forms.ModelForm):
    class Meta:
        model = Client_Booking_ApartmentForm
        fields = '__all__'
        widgets = {
            'Check_In':widgets.SelectDateWidget(
                                    empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                    ),
            'Check_Out':widgets.SelectDateWidget(
                                    empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                    )
        }
        
        