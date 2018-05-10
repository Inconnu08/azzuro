# azzurro URL Configuration

from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from azzurro import settings

urlpatterns = [
    url(r'^', include('core.urls')),
    path('admin/', admin.site.urls),
    url(r'^products/', include('products.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)