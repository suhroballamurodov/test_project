from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('product_list',ProductListApiView.as_view(), name = 'product_list'),
    path('material_list',MaterialListApiView.as_view(), name = 'material_list'),
    path('warehous_list',WarehouseListApiView.as_view(), name = 'warehous_list'),
    path('result',ProductMaterialList.as_view(), name = 'result'),
]