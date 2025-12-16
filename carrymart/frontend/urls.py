from django.urls import path
from .views import login_page, register_page, products_page, dashboard_page, cart_page, my_orders_page, payment_page

urlpatterns = [
    path("", login_page, name="login"),
    path("register-page/", register_page, name="register"),
    path("products-page/", products_page, name="products"),
    path("dashboard/", dashboard_page, name="dashboard"),
    path("cart/", cart_page, name="cart_page"),  
    path("orders/", my_orders_page, name="my-orders-page"),
    path("payment-page/<int:order_id>/", payment_page, name="payment"),
    path("payment-page/", payment_page, name="payment"),


]
