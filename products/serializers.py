from rest_framework import serializers
from .models import Product
from category.models import Category  

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',  
        write_only=True  
    )
    category_name = serializers.StringRelatedField(source='category', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category_id', 'category_name', 'image']

