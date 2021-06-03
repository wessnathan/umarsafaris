from django import forms
from django.forms import widgets
from .models import Booking_ApartmentsForm

class User_BookingForm(forms.ModelForm):

    class Meta:
            model = Booking_ApartmentsForm
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