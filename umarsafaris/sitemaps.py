from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from apartment.models import Umarsafarisrooms
from carbooking.models import Cars_Available
from safarisapp.models import *

class HomeViewSitemap(Sitemap):
    def items(self):
        return ['home'] # path's name
    def location(self, item):
        return reverse(item)
    
class ApartmentsViewSitemap(Sitemap):
    def items(self):
        return ['apartments'] # path's name
    def location(self, item):
        return reverse(item)
    
class CarsViewSitemap(Sitemap):
    def items(self):
        return ['car'] # path's name
    def location(self, item):
        return reverse(item)
    
class CarsDetailViewSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    
    def items(self):
        return Cars_Available.objects.all() # path's name
    
    def lastmod(self, obj):
        return obj.publish 
    
class ApartmentsDetailViewSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    
    def items(self):
        return Umarsafarisrooms.objects.all() # path's name
    
    def lastmod(self, obj):
        return obj.slug