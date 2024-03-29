# Generated by Django 3.0.5 on 2021-06-12 05:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars_Available',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='umarapp')),
                ('model', models.CharField(choices=[('Toyota Prado', (('Prado Tx', 'Prado Tx'), ('Toyota LandCruiser', 'Toyota LandCruiser'))), ('RANGE ROVER', (('RANGE ROVER SPORT', 'RANGE ROVER SPORT'), ('RANGE ROVER VELAR', 'RANGE ROVER VELAR'), ('RANGE ROVER EVOQUE', 'RANGE ROVER EVOQUE'), ('RANGE ROVER DNA', 'RANGE ROVER DNA'))), ('Mercedes-Benz', (('Mercedes-Benz AMG GT', 'Mercedes-Benz AMG GT'), ('Mercedes-Benz Maybach', 'Mercedes-Benz Maybach'), ('Mercedes-Benz CLS', 'Mercedes-Benz CLS'), ('Mercedes-Benz E CLASS', 'Mercedes-Benz E CLASS')))], default='0', max_length=50)),
                ('milage', models.IntegerField(default=None)),
                ('seater', models.IntegerField(default=None)),
                ('lugage', models.IntegerField(default=None)),
                ('airconditioner', models.BooleanField(default=None)),
                ('automatic', models.BooleanField(default=None)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('description', models.TextField(default=None, max_length=250)),
                ('fuelpolicy', models.TextField(default='Full to Full', max_length=250)),
                ('carpolicy', models.TextField(default='Meet the renting locations minimum age requirements.Have a valid drivers license.')),
            ],
            options={
                'verbose_name_plural': 'Posted Available Cars and Their Features Umarsafaris',
            },
        ),
        migrations.CreateModel(
            name='Current_caruser_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Second_Name', models.CharField(max_length=20)),
                ('ID_No', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=30)),
                ('Contact', models.CharField(max_length=14)),
                ('Check_In', models.DateField(default=django.utils.timezone.now)),
                ('Check_In_Time', models.TimeField(default=django.utils.timezone.now)),
                ('Check_Out', models.DateField(default=django.utils.timezone.now)),
                ('Check_Out_Time', models.TimeField(default=django.utils.timezone.now)),
                ('carpicked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carbooking.Cars_Available')),
            ],
            options={
                'verbose_name_plural': ' Booked Cars Client Information',
            },
        ),
    ]
