from django.urls import path

<<<<<<< HEAD
from .views import shop_index, groups_list, products_list, orders_list
=======
from .views import shop_index, groups_list
>>>>>>> master

url_name = "shopapp"

urlpatterns = [
    path('', shop_index, name='index'),
    path('groups/', groups_list, name='groups_list'),
<<<<<<< HEAD
    path('products', products_list, name='products_list'),
    path('orders', orders_list, name='orders_list'),
]
=======
]

>>>>>>> master
