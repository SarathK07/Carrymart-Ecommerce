"""Frontend simple page views.

These views render the static templates used by the frontend app
for login, registration, product listing, cart, orders, dashboard
and payment pages. They keep logic minimal and only provide
template context where needed.
"""

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



from django.shortcuts import render

# Renders the login page template.
def login_page(request):
    return render(request, "login.html")

# Renders the registration page template.
def register_page(request):
    return render(request, "register.html")

# Renders the main products listing page.
def products_page(request):
    return render(request, "products/products.html")

# Renders the admin/user dashboard page.
def dashboard_page(request):
    return render(request, "products/dashboard.html")

# Renders the cart page showing current user's cart items.
def cart_page(request):
    return render(request, 'products/cart_page.html')

# Renders the current user's orders page.
def my_orders_page(request):
    return render(request, 'products/my_orders_page.html')

# Renders the payment page for a given order.
# `order_id` is optional; template receives it in context.
def payment_page(request, order_id=None):
    return render(
        request,
        "products/payment_page.html",
        {"order_id": order_id}
    )