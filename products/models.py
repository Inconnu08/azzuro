import os
import random

from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female"),
    ("not specified", "not specified")
)


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class AttributeType(models.Model):
    name = models.CharField(max_length=50, blank=False)
    value = models.CharField(max_length=100)

    def __str__(self):
        return "{}-{}".format(self.name, self.value)


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def only_women(self):
        return self.filter(gender="female", active=True)

    def only_men(self):
        return self.filter(gender="male", active=True)

    def only_accessories(self):
        return self.filter(accessories=True, active=True)

    def only_designer_dresses(self):
        return self.filter(designer_dress=True, active=True)

    def only_wedding_collection(self):
        return self.filter(wedding_collection=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(categories__title__icontains=query) |
                   Q(brand__name__icontains=query)
                   )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.active().filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):  # Product.objects.featured()
        return self.get_queryset().featured()

    def only_female(self):
        return self.get_queryset().only_women()

    def only_male(self):
        return self.get_queryset().only_men()

    def get_accessories(self):
        return self.get_queryset().only_accessories()

    def get_wedding_collections(self):
        return self.get_queryset().only_wedding_collection()

    def get_designer_dresses(self):
        return self.get_queryset().only_designer_dresses()

    def get_by_id(self, _id):
        qs = self.get_queryset().filter(id=_id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


class Brand(models.Model):
    name = models.CharField(max_length=225)
    logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    @property
    def get_products(self):
        return Products.objects.filter(categories__title=self.title)

    class Meta:
        verbose_name_plural = "categories"


class Products(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    brand = models.ForeignKey(Brand, related_name='brand', null=True, blank=True, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(default=timezone.now)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    accessories = models.BooleanField(default=False)
    designer_dress = models.BooleanField(default=False)
    wedding_collection = models.BooleanField(default=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="male")

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=(self.id,))

    def __str__(self):
        if self.brand:
            return self.brand.name + " " + self.title
        else:
            return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Products'
