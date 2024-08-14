import uuid
from django.db import models


class Product(models.Model):
    productname = models.CharField(max_length=255, null=True, blank=True)
    product_code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.productname


class Material(models.Model):
    material_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.material_name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.product.productname} - {self.material.material_name}: Quantity - {self.quantity}'


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.material.material_name} - {self.remainder} qolgani - {self.price} UZS'
