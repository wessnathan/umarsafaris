from carbooking.models import Current_caruser_booking
from rest_framework import serializers


class Current_caruser_bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Current_caruser_booking
        fields = ['id', 'Email', 'Check_In']