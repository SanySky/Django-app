from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    """Create products"""

    def handle(self, *args, **options):
        self.stdout.write('Create products')

        products_names = [
            "Laptop",
            "Desktop",
            "Smartphone"
        ]
        product = Product("asdasd")
        product.save()

        self.stdout.write(self.style.SUCCESS("Products created"))

