from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.models import Order
from .models import Payment
import uuid


class CreatePaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        # ✅ Check if already paid
        if Payment.objects.filter(order=order).exists():
            return Response({"message": "Payment already completed for this order"}, status=400)

        payment_id = str(uuid.uuid4())

        payment = Payment.objects.create(
            user=request.user,
            order=order,
            payment_id=payment_id,
            amount=order.total_price,
            status='success'
        )

        # ✅ Update order status
        order.status = 'order_placed'
        order.save()

        return Response({
            "message": "Payment successful, order placed",
            "payment_id": payment.payment_id
        })
