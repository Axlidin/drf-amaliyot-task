from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouse


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'product_code']
    search_fields = ['productname', 'product_code']


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material_name']
    search_fields = ['material_name']


class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ['product', 'material', 'quantity']
    search_fields = ['product__produtyname', 'material__materialname']


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['material', 'remainder', 'price']
    search_fields = ['material__material_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(Warehouse, WarehouseAdmin)