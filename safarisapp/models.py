from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from django import forms
from django.urls import reverse


class Apartmentsbase(models.Model):
    Rooms = models.IntegerField()
    Name = models.CharField(default='Room Name and building', max_length=150)
    Photo1 = models.ImageField(default='default.jpg', upload_to='apartments')
    Photo2 = models.ImageField(default='default.jpg', upload_to='apartments')
    Photo3 = models.ImageField(default='default.jpg', upload_to='apartments')
    Photo4 = models.ImageField(default='default.jpg', upload_to='apartments')
    Photo5 = models.ImageField(default='default.jpg', upload_to='apartments')
    slug = models.SlugField(default='0')
    Description = models.TextField()
    def __str__(self):
        return self.Rooms
    
    def get_absolute_url(self):
        return reverse('apartment-detail', args=[self.slug])
    
    def __str__(self):
        return str(self.Name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.Name)
        
        try:
            this = Image.objects.get(id=self.id)
            if this.Photo1 != self.Photo1:
                this.Photo1.delete(save=False)
            elif this.Photo2 != self.Photo2:
                this.Photo2.delete(save=False)
            elif this.Photo3 != self.Photo3:
                this.Photo3.delete(save=False)
            elif this.Photo4 != self.Photo4:
                this.Photo4.delete(save=False)
            else:
                this.Photo5.delete(save=False)
                
        except:
            pass  # when new photo then we do nothing, normal case
        super(Apartmentsbase, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Available apartments and Rooms"
        
class SliderImage(models.Model):
    Background_Images = models.ImageField(default='default.jpg', upload_to='media/slider')
    
    def save(self, *args, **kwargs):
        super(SliderImage, self).save(*args, **kwargs)
        
    
    
class Cargallery(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='gallery')
    
    
class Carfeatures(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField( upload_to='umarapp', null=True)
    model = models.CharField(max_length=50, default='0')
    milage = models.IntegerField(default=None)
    seater = models.IntegerField(default=None)
    lugage = models.IntegerField(default=None)
    airconditioner = models.BooleanField(default=None)
    automatic = models.BooleanField(default=None)
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField()
    description = models.TextField(max_length=250, default=None)
    fuelpolicy = models.TextField(max_length=250, default='Full to Full')
    carpolicy = models.TextField(default='Meet the renting locations minimum age requirements.Have a valid drivers license.')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('car-detail', args=[self.slug])
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        
        try:
            this = Image.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Carfeatures, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Available Cars and Their Features"
        
        
    
class Current_user_booking(models.Model):
    First_Name = models.CharField(max_length=20)
    Second_Name = models.CharField(max_length=20)
    carpicked = models.CharField(max_length=10, default='none')
    ID_No = models.CharField(max_length=15)
    Email = models.EmailField(max_length=30)
    Contact = models.CharField(max_length=14)
    Booking_from = models.DateField()
    Booking_to = models.DateField()
    
    class Meta:
        verbose_name_plural = " Renting Client Details"
        
    def __str__(self):
        return f'{self.First_Name} {self.Second_Name} has rented {self.carpicked} from {self.Booking_from} till {self.Booking_to}'
        
        
class About(models.Model):
    about = models.CharField(max_length=400)
    address = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    Location = models.CharField(max_length=250)
    
    class Meta:
        verbose_name_plural = " About Bussiness and Location"
        
class Contact(models.Model):
    fname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = " Contact Us Client Details"
        
    def __str__(self):
        return f'{self.fname} is inquiring about{self.title}. Contact through {self.tel} or Send feed back mail {self.email} '
