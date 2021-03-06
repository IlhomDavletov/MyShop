from django.shortcuts import render

from product.models import *


def home_page(request):
    categories = Category.objects.all()
    return render(request, 'product/home.html', {'categories':categories})


def product_list(request, slug):
    products = Product.objects.filter(category__slug=slug)
    return render(request, 'product/list.html', locals())
