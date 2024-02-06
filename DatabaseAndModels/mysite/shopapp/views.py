from timeit import default_timer
from .models import Product, Order
from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.shortcuts import render


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


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'myauth/order_list.html', context=context)
