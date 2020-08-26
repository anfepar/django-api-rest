from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all().order_by("-created")
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
