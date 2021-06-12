from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image

class Cars_Available(models.Model):
    categories = (
        ('Toyota Prado', (('Prado Tx', 'Prado Tx'),('Toyota LandCruiser', 'Toyota LandCruiser'))),
        ('RANGE ROVER', (('RANGE ROVER SPORT', 'RANGE ROVER SPORT'),('RANGE ROVER VELAR','RANGE ROVER VELAR'), ('RANGE ROVER EVOQUE','RANGE ROVER EVOQUE'), ('RANGE ROVER DNA', 'RANGE ROVER DNA'))),
        ('Mercedes-Benz', (('Mercedes-Benz AMG GT', 'Mercedes-Benz AMG GT'), ('Mercedes-Benz Maybach','Mercedes-Benz Maybach'),('Mercedes-Benz CLS','Mercedes-Benz CLS'), ('Mercedes-Benz E CLASS', 'Mercedes-Benz E CLASS'))),
    )
        
        
    name = models.CharField(max_length=50)
    image = models.ImageField( upload_to='umarapp', null=True)
    model = models.CharField(max_length=50, choices=categories, default='0')
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
        super(Cars_Available, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Posted Available Cars and Their Features Umarsafaris"
        
        
class Current_caruser_booking(models.Model):
    First_Name = models.CharField(max_length=20)
    Second_Name = models.CharField(max_length=20)
    carpicked = models.ForeignKey(Cars_Available, on_delete=models.CASCADE)
    ID_No = models.CharField(max_length=15)
    Email = models.EmailField(max_length=30)
    Contact = models.CharField(max_length=14)
    Check_In = models.DateField(default=timezone.now)
    Check_In_Time = models.TimeField(default=timezone.now)
    Check_Out = models.DateField(default=timezone.now)
    Check_Out_Time = models.TimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = " Booked Cars Client Information"
        
    def __str__(self):
        return f'{self.First_Name} {self.Second_Name} has rented {self.carpicked} from {self.Check_Out} {self.Check_In_Time} till {self.Check_Out} {self.Check_Out_Time}'
        
        