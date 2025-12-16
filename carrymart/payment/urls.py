from django.urls import path
from .views import CreatePaymentAPIView

urlpatterns = [
    path('pay/<int:order_id>/', CreatePaymentAPIView.as_view()),
]
