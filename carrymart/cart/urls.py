from django.urls import path
from .views import (
    AddToCartAPIView,
    ViewCartAPIView,
    UpdateCartItemAPIView,
    DeleteCartItemAPIView
)

urlpatterns = [
    path('add/', AddToCartAPIView.as_view()),
    path('viewcart/', ViewCartAPIView.as_view()),
    path('update/', UpdateCartItemAPIView.as_view()),
    path('delete/', DeleteCartItemAPIView.as_view()),
]
