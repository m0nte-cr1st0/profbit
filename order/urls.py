from django.urls import path

from order.views import OrdersList, TopProductView

urlpatterns = [
    path("", OrdersList.as_view(), name="orders-list"),
    path("rating", TopProductView.as_view(), name="products-list")
]
