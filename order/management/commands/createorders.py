from datetime import datetime, timedelta
from random import randint

from django.core.management.base import BaseCommand

from order.models import Order, OrderItem


class Command(BaseCommand):
    help = 'Create orders'

    def add_arguments(self, parser):
        """Parse arguments from command line"""
        parser.add_argument('orders_count', nargs='+', type=int)

    def handle(self, *args, **options):
        """Create orders and order items"""
        start_datetime = "01.01.2018 09:00"
        orders_count = options['orders_count'][0]
        Order.objects.bulk_create([
            Order(
                number=ind + 1,
                created_date=datetime.strptime(start_datetime, "%m.%d.%Y %H:%M") + timedelta(hours=ind)
            )
            for ind in range(orders_count)
        ])
        for order in Order.objects.all():
            OrderItem.objects.bulk_create([
                OrderItem(
                    order=order,
                    product_name=f"Товар-{randint(1, 100)}",
                    product_price=randint(100, 9999),
                    amount=randint(1, 10)
                )
                for i in range(randint(1, 5))
            ])
        self.stdout.write(self.style.SUCCESS(
            f"Successfully created {orders_count} orders"
        ))
