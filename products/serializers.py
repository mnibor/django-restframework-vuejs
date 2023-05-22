from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Category, Product

class ProductFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name='category', lookup_expr='exact')
    name = filters.CharFilter(method='filter_by_search', lookup_expr='icontains')

    def filter_by_search(self, queryset, value):
        return queryset.filter(name__icontains=value) | queryset.filter(description__icontains=value)

    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'name': ['icontains'],
        }

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    price_type_description = serializers.ReadOnlyField(source='get_price_type_display')

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'category', 'category_name', 'description', 'price', 'price_type', 'price_type_description')
        filterset_class = ProductFilter

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
