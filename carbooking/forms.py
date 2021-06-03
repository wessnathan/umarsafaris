from django import forms
from django.forms import widgets
from .models import Current_caruser_booking

class Car_BookingForm(forms.ModelForm):

    class Meta:
            model = Current_caruser_booking
            fields = '__all__'
            widgets = {
                'Check_In':widgets.SelectDateWidget(
                                        empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                        ),
                'Check_In_Time':forms.TimeInput(attrs={'type': 'time'}),
                'Check_Out_Time':forms.TimeInput(attrs={'type': 'time'}),
                'Check_Out':widgets.SelectDateWidget(
                                        empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                        )
            }