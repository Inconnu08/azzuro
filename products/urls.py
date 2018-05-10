from django.conf.urls import url
from django.conf.urls.static import static

from azzurro import settings
from products import views

urlpatterns = [
    url(r'^categories/male/$', views.categories_m, name='categories-male'),
    url(r'^categories/female/$', views.categories_f, name='categories-female'),
    url(r'^categories_list/$', views.product_list, name='product_list'),
    url(r'^(?P<id>[\w-]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

