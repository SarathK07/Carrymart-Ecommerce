from django.urls import path
from .views import PlaceOrderAPIView, MyOrdersAPIView, AdminAllOrdersAPIView

urlpatterns = [
    path('place/', PlaceOrderAPIView.as_view()),
    path('my/', MyOrdersAPIView.as_view()),
    path('all/', AdminAllOrdersAPIView.as_view()),
]
