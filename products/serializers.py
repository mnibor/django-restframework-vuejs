from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'category', 'description', 'price', 'price_type')
        # fields = '__all__'          # Obtengo TODOS los campos de la tabla en el orden en que están generados en la tabla de SQLite

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'