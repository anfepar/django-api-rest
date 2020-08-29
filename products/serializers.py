from products.models import Product, Color, Size
from rest_framework import serializers

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ["name", "ref"]

class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ["name"]

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    colors = ColorSerializer(read_only=True,many=True)
    sizes = SizeSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ["pk", "name","price","picture","description","created","modified", "category",  "sizes", "colors"]