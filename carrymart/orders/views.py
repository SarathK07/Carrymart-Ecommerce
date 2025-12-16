from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from cart.models import Cart, CartItem
from .models import Order, OrderItem

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer



class PlaceOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        # get cart
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"error": "Cart is empty"}, status=400)

        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            return Response({"error": "No items in cart"}, status=400)

        total = 0
        order = Order.objects.create(user=user)

        for item in cart_items:
            item_total = item.product.price * item.quantity
            total += item_total

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        order.total_price = total
        order.save()

        # clear cart after order
        cart_items.delete()

        return Response({"message": "Order placed successfully", "order_id": order.id})


"""class MyOrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')

        data = []
        for order in orders:
            data.append({
                "id": order.id,
                "status": order.status,
                "total_price": order.total_price,
                "created_at": order.created_at
            })

        return Response(data)"""
    
    
"""class MyOrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    """


class MyOrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = (
            Order.objects
            .filter(user=request.user)
            .prefetch_related('items', 'items__product')
            .order_by('-created_at')
        )

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)



class AdminAllOrdersAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        orders = Order.objects.all().order_by('-created_at')

        data = []
        for order in orders:
            data.append({
                "id": order.id,
                "user": order.user.username,
                "status": order.status,
                "total_price": order.total_price,
                "created_at": order.created_at
            })

        return Response(data)
