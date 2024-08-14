from django.urls import path
from .views import ProductView, MaterialView, WarehouseView, ProductMaterialView, MaterialRequirementView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('ombor/', WarehouseView.as_view()),
    path('p-m/', ProductMaterialView.as_view()),
    path('material/', MaterialView.as_view()),
    path('warehouse/', MaterialRequirementView.as_view()),
]