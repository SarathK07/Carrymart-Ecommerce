from django.shortcuts import render

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def products_page(request):
    return render(request, "products/products.html")

#dashboard view
def dashboard_page(request):
    return render(request, "products/dashboard.html")

def cart_page(request):
    return render(request, 'products/cart_page.html')


def my_orders_page(request):
    return render(request, 'products/my_orders_page.html')


def payment_page(request, order_id=None):
    return render(
        request,
        "products/payment_page.html",
        {"order_id": order_id}
    )



