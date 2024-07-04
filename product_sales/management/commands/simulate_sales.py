from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from product_sales.models import Product, Sale
from django.utils import timezone
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'Simulate 500 product sales'

    def handle(self, *args, **options):
        # Create products
        products = [
            Product.objects.create(name='Product A', price=100),
            Product.objects.create(name='Product B', price=200),
            Product.objects.create(name='Product C', price=300),
            Product.objects.create(name='Product D', price=400),
            Product.objects.create(name='Product E', price=500),
        ]

        # Get all users
        users = User.objects.all()

        # Simulate 500 product sales
        for _ in range(500):
            user = random.choice(users)
            product = random.choice(products)
            Sale.objects.create(user=user, product=product, sale_date=timezone.now())

        self.stdout.write(self.style.SUCCESS('Successfully simulated 500 product sales'))
