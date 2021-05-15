# Generated by Django 3.0.5 on 2021-05-13 04:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=100)),
                ('Telephone', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': ' About Bussiness and Location',
            },
        ),
        migrations.CreateModel(
            name='Apartmentsbase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rooms', models.IntegerField()),
                ('Name', models.CharField(default='Room Name and building', max_length=150)),
                ('Photo1', models.ImageField(default='default.jpg', upload_to='apartments')),
                ('Photo2', models.ImageField(default='default.jpg', upload_to='apartments')),
                ('Photo3', models.ImageField(default='default.jpg', upload_to='apartments')),
                ('Photo4', models.ImageField(default='default.jpg', upload_to='apartments')),
                ('Photo5', models.ImageField(default='default.jpg', upload_to='apartments')),
                ('slug', models.SlugField(default='0')),
                ('Description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Available apartments and Rooms',
            },
        ),
        migrations.CreateModel(
            name='Carfeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='umarapp')),
                ('model', models.CharField(default='0', max_length=50)),
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
                'verbose_name_plural': 'Available Cars and Their Features',
            },
        ),
        migrations.CreateModel(
            name='Cargallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': ' Contact Us Client Details',
            },
        ),
        migrations.CreateModel(
            name='Current_user_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Second_Name', models.CharField(max_length=20)),
                ('carpicked', models.CharField(default='none', max_length=10)),
                ('ID_No', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=30)),
                ('Contact', models.CharField(max_length=14)),
                ('Booking_from', models.DateField()),
                ('Booking_to', models.DateField()),
            ],
            options={
                'verbose_name_plural': ' Renting Client Details',
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Background_Images', models.ImageField(default='default.jpg', upload_to='media/slider')),
            ],
        ),
    ]