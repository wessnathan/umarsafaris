from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image


# Create your models here.


class Umarsafarisrooms(models.Model):
    select_apt = (
        ('DEL', (('DL1', 'D1'),('DL2', 'D2'),('DL3', 'D3'),('DL4', 'D4'))),
        ('Rook', (('RK1', 'RK1'),('RK2', 'RK2'),('RK3', 'RK3'),('RK4', 'RK4'))),
        ('Bishop', (('BSP1', 'BSP1'),('BSP2', 'BSP2'),('BSP3', 'BSP3'),('BSP4', 'BSP4'))),
        ('Castle', (('CST1', 'CST1'),('CST2', 'CST2'),('CST3', 'CST3'),('CST4', 'CST4'))),
    )
    Rooms = models.CharField(max_length=10, choices=select_apt, default='room')
    Name = models.CharField(max_length=100, default='Enter name of apartment')
    Beds = models.CharField(max_length=1, default=0)
    Description = models.TextField()
    Photo1 = models.ImageField(default='default.jpg', upload_to='apartments')
    Photo2 = models.ImageField(default='default.jpg', upload_to='apartments')
    Photo3 = models.ImageField(default='default.jpg', upload_to='apartments')
    Photo4 = models.ImageField(default='default.jpg', upload_to='apartments')
    Photo5 = models.ImageField(default='default.jpg', upload_to='apartments')
    slug = models.SlugField(default='0')
    Room_details = models.CharField(max_length=300, default=' ')
    
    def __str__(self):
        return f'{self.Name} type {self.Rooms} has {self.Beds}'
    
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
        super(Umarsafarisrooms, self).save(*args, **kwargs)
    
    
    class Meta:
        verbose_name_plural = "Posted UmarSafaris Apartments "
        
    
    
class Booking_ApartmentsForm(models.Model):
    
    Apartment = models.ForeignKey(Umarsafarisrooms, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    ID_No = models.CharField(max_length=30)
    Tel =models.CharField(max_length=13)
    Check_In = models.DateField(default=timezone.now)
    Check_In_Time = models.TimeField(default=timezone.now)
    Check_Out = models.DateField(default=timezone.now)
    Check_Out_Time =models.TimeField(default=timezone.now)
    
    
    def __str__(self):
        return f'{self.Name} has Booked Apartment{self.Apartment}  from{self.Check_In}{self.Check_In_Time} to {self.Check_Out}{self.Check_Out_Time}, {self.Email}, {self.Tel}, {self.ID_No}'
        
    class Meta:
        verbose_name_plural = " Apartment Clients Booking Information"
        