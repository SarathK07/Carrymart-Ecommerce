# cart/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from products.models import Product

class AddToCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        if not product_id:
            return Response({"error": "product_id is required"}, status=400)

        cart, _ = Cart.objects.get_or_create(user=request.user)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity

        cart_item.save()
        return Response({"message": "Added to cart"})


class UpdateCartItemAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        item_id = request.data.get("item_id")
        quantity = int(request.data.get("quantity", 1))

        try:
            item = CartItem.objects.get(id=item_id, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)

        if quantity <= 0:
            item.delete()
            return Response({"message": "Item removed"})
        else:
            item.quantity = quantity
            item.save()
            return Response({"message": "Quantity updated"})


class DeleteCartItemAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        item_id = request.data.get("item_id")

        try:
            item = CartItem.objects.get(id=item_id, cart__user=request.user)
            item.delete()
            return Response({"message": "Item deleted"})
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)


class ViewCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        items = CartItem.objects.filter(cart=cart)
        data = []

        for i in items:
            # Include full image URL
            image_url = request.build_absolute_uri(i.product.image.url) if i.product.image else ""

            data.append({
                "id": i.id,
                "product_id": i.product.id,
                "product_name": i.product.name,
                "price": str(i.product.price),
                "quantity": i.quantity,
                "image": image_url,  # <-- added
            })

        return Response(data)
