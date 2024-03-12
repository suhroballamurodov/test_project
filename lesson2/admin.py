from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_quantity')
    search_fields = ['product_name']

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material_name']
    search_fields = ['material_name']


class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product', 'material', 'quantity')
    search_fields = ['product']

class WarehousAdmin(admin.ModelAdmin):
    list_display = ('material', 'remainder', 'price')
    search_fields = ['remainder','price']


admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(Warehouse, WarehousAdmin)
