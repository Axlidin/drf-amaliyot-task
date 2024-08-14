from rest_framework import generics
from .serializers import WarehouseSerializer, ProductMaterialSerializer, MaterialSerializer
from .serializers import ProductSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductMaterial, Warehouse, Material


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MaterialView(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class WarehouseView(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductMaterialView(generics.ListAPIView):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer



class MaterialRequirementView(views.APIView):

    def post(self, request, *args, **kwargs):
        product_code = request.data.get("product_code")
        quantity = request.data.get("quantity")

        try:
            product = Product.objects.get(product_code=product_code)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        required_materials = ProductMaterial.objects.filter(product=product)
        result = {
            "result": []
        }

        product_data = {
            "product_name": product.productname,
            "product_qty": quantity,
            "product_materials": []
        }

        for material in required_materials:
            material_name = material.material.material_name
            total_required_qty = material.quantity * quantity

            warehouses = Warehouse.objects.filter(material=material.material).order_by('price')
            remaining_qty = total_required_qty

            for warehouse in warehouses:
                if remaining_qty <= 0:
                    break

                if warehouse.remainder > 0:
                    if warehouse.remainder >= remaining_qty:
                        product_data["product_materials"].append({
                            "warehouse_id": warehouse.id,
                            "material_name": material_name,
                            "qty": remaining_qty,
                            "price": warehouse.price
                        })
                        remaining_qty = 0
                    else:
                        product_data["product_materials"].append({
                            "warehouse_id": warehouse.id,
                            "material_name": material_name,
                            "qty": warehouse.remainder,
                            "price": warehouse.price
                        })
                        remaining_qty -= warehouse.remainder

            if remaining_qty > 0:
                product_data["product_materials"].append({
                    "warehouse_id": None,
                    "material_name": material_name,
                    "qty": remaining_qty,
                    "price": None
                })

        result["result"].append(product_data)

        return Response(result, status=status.HTTP_200_OK)
