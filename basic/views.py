from django.shortcuts import render
from .models import Setting, Category, Product


def index(request):
    setting = Setting.objects.get(pk=1)
    product = Product.objects.all().order_by('-id')
    context = {
        'setting': setting,
        'products': product,
    }
    return render(request, 'index.html', context)


def category_products(request, pk):
    category = Category.objects.filter(pk=pk)
    product = Product.objects.filter(category__id=pk)
    context = {
        'category': category,
        'products': product,
    }
    return render(request, 'category_product.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})
