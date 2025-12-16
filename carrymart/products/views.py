from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(APIView):
    
    # Logged-in users only (admin + customers can view)
    permission_classes = [IsAuthenticated]

    # GET: list products (customer + admin)
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # POST: only admin can create
    def post(self, request):
        if not request.user.is_staff:
            return Response({"error": "Only admin can add products"}, status=403)

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductDetailAPIView(APIView):

    # Logged-in users only
    permission_classes = [IsAuthenticated]

    # GET: retrieve product (customer + admin)
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # PUT: only admin can update
    def put(self, request, pk):
        if not request.user.is_staff:
            return Response({"error": "Only admin can update products"}, status=403)

        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE: only admin can delete
    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response({"error": "Only admin can delete products"}, status=403)

        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({"message": "Deleted successfully"}, status=204)
