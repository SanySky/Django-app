from django.contrib import admin
from shopapp.models import Product


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product)
