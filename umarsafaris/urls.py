from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

sitemaps = {
    'home': HomeViewSitemap,
    'apartments':ApartmentsViewSitemap,
    'car':CarsViewSitemap,
    'car-detail':CarsDetailViewSitemap,
    'apartment-detail':ApartmentsDetailViewSitemap,
}

urlpatterns = [
    path('', include('safarisapp.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]

urlpatterns += [ path(r'^tz_detect/', include('tz_detect.urls')),]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)