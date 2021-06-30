from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image


class ImagesOnHome(models.Model):
    title = models.CharField(max_length=100, default=' ')
    psg = models.CharField(max_length=200, default=' ')
    imghome = models.ImageField(upload_to='safarisapp/images/gallery/fulls')
    
    class Meta:
        verbose_name_plural = "Images and Information on the first page"
        
    def __str__(self):
        return self.title


class SendMessage(models.Model):
    mesg = models.TextField()
    profile = models.ImageField(upload_to='userfeedback_profile')
    email = models.EmailField()
    dt =models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        verbose_name_plural = " User Posted FeedBack"
        
    def __str__(self):
        return f'{self.email} posted on {self.dt}'


class About(models.Model):
    about = models.CharField(max_length=400)
    address = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    Location = models.CharField(max_length=250)
    
    class Meta:
        verbose_name_plural = " About Bussiness and Location"
        
    def get_absolute_url(self):
        return reverse('About', args=(self.pk,))
        
class Ourteam(models.Model):
    name = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='Teamphotos')
    position = models.CharField(max_length=15)
    email = models.EmailField()
    dates = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = " Umar Safaris Team"
        
    def __str__(self):
        return f'{self.email} posted on {self.dates}'
    
    def get_absolute_url(self):
        return reverse('Ourteam', args=(self.pk,))
        
        
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
