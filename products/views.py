from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView
from products import models
from products.models import Products


class ProductDetailView(DetailView):
    """
    class based product detail view
    """
    model = models.Products
    pk_url_kwarg = 'id'
    template_name = 'products/product_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(**kwargs)
    #     obj = self.get_object()
    #     context['related_products'] = sorted(self.model.objects.get_related_products(obj)[:5],
    #  key= lambda x :random.random())
    #     return context


def categories_m(request):
    category_ids = Products.objects.filter(gender='male').values_list('categories', flat=True)
    query_Set = models.Category.objects.get_queryset().order_by('id').filter(id__in=category_ids)
    page = request.GET.get('page', 1)
    paginator = Paginator(query_Set, 20)
    try:
        cat = paginator.page(page)
    except PageNotAnInteger:
        cat = paginator.page(1)
    except EmptyPage:
        cat = paginator.get_page(paginator.num_pages)
    return render(request, 'products/categories.html', {'categories': cat})


def categories_f(request):
    category_ids = Products.objects.filter(gender='female').values_list('categories', flat=True)
    query_Set = models.Category.objects.filter(id__in=category_ids)
    page = request.GET.get('page', 1)
    paginator = Paginator(query_Set, 20)
    try:
        cat = paginator.page(page)
    except PageNotAnInteger:
        cat = paginator.page(1)
    except EmptyPage:
        cat = paginator.get_page(paginator.num_pages)
    return render(request, 'products/categories.html', {'categories': cat, 'female': True})


def product_list(request):
    query_Set = Products.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(query_Set, 16)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'products/product_list.html', {'numbers': numbers})
