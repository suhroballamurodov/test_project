from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Warehouse
        fields = '__all__'

class ProductMaterialSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ProductMaterial
        fields = '__all__'