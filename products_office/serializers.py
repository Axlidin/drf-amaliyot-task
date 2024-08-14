from rest_framework import serializers
from .models import Product, ProductMaterial, Material, Warehouse


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('productname', 'product_code')

        def __str__(self):
            return f'{self.productname} - {self.product_code}'



class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('material_name', )

    def __str__(self):
        return self.material_name


class ProductMaterialSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.productname')
    material = serializers.CharField(source='material.material_name')

    class Meta:
        model = ProductMaterial
        fields = ('product', 'material', 'quantity')



class WarehouseSerializer(serializers.ModelSerializer):
    material = serializers.CharField(source='material.material_name')


    class Meta:
        model = Warehouse
        fields = ('material', 'remainder', 'price')