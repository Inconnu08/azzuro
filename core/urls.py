from django.conf.urls import url

from core.views import SearchProductView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'about/$', views.about, name='about'),
    url(r'contact-us/$', views.contact, name='contact'),
    url(r'search/$', SearchProductView.as_view(), name='query'),
]
