# Generated by Django 3.0.5 on 2021-05-26 06:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('safarisapp', '0004_client_booking_apartmentform'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_booking_apartmentform',
            name='Check_In',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client_booking_apartmentform',
            name='Check_Out',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]