from timeit import default_timer


from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.shortcuts import render, redirect, reverse

from .forms import ProductForm, OrderForm
from .models import Product, Order


def shop_index(request: HttpRequest):
    products = [
        ("Laptop", 195),
        ("Desktop", 295),
        ("Smartphone", 995),

    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, 'myauth/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'myauth/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'myauth/products_list.html', context=context)


def create_product(request: HttpRequest):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            #Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse("myauth:products_list")
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'myauth/product_form.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'myauth/order_list.html', context=context)


def create_order(request: HttpRequest):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            #Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse("myauth:orders_list")
            return redirect(url)
    else:
        form = OrderForm()
    context = {
        'form': form,
    }
    return render(request, 'myauth/order_form.html', context=context)
