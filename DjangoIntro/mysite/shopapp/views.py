from timeit import default_timer

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


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
