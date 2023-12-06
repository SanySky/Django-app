from timeit import default_timer

<<<<<<< HEAD
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import Group
from django.shortcuts import render
from .models import Product, Order
=======
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
>>>>>>> master


def shop_index(request: HttpRequest):
    products = [
        ("Laptop", 195),
        ("Desktop", 295),
        ("Smartphon", 995),

    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)
<<<<<<< HEAD


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)

=======
>>>>>>> master
