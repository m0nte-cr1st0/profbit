from collections import defaultdict

from django.db import models
from django.db.models import F, Sum
from django.views.generic import ListView

from order.models import Order, OrderItem


class OrdersList(ListView):
    """Orders list with order sum"""
    queryset = Order.objects.prefetch_related("order_item").annotate(
        order_sum=Sum(
            F("order_item__product_price") * F("order_item__amount"),
            output_field=models.FloatField()
        )
    )


class TopProductView(ListView):
    """Top-20 rating of products"""
    model = OrderItem
    template_name = "order/product_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Top-20 rating of products ordered by total cost in all orders.
        Most popular product by sum of amount in all orders.
        """
        context_data = super(TopProductView, self).get_context_data()

        products = defaultdict(list)
        for item in OrderItem.objects.values(
                "product_name", "product_price", "amount", "order__number", "order__created_date"
        ):
            products[item['product_name']].append([
                item['order__created_date'],
                item['order__number'],
                item["product_price"] * item["amount"],
                item["amount"]
            ])

        top_products = sorted(
            products.items(), key=lambda i: sum(y[2] for y in i[1]), reverse=True
        )[:20]
        most_popular = sorted(
            products.items(), key=lambda i: sum(y[3] for y in i[1]), reverse=True
        )[0][0]

        context_data["products"] = top_products
        context_data["most_popular"] = most_popular
        return context_data
