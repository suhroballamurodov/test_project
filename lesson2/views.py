from django.http import HttpResponse
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializers import *


def home(request):
    '''Saytni ishlayotganligini bilish uchun test page'''
    return HttpResponse('This is my applications for test_project')


class ProductListApiView(APIView):
    '''Barcha Productlarni olish uchun API'''
    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response({"Productlar ro'yxati":serializer.data})


class MaterialListApiView(APIView):
    '''Barcha Materiallarni olish uchun API'''
    def get(self,request):
        material = Material.objects.all()
        serializer = MaterialSerializer(material, many=True)
        return Response({"Materiallar ro'yxati: ":serializer.data})


class ProductMaterialListApiView(APIView):
    '''Barcha Product-Materiallarni olish uchun API'''
    def get(self,request): 
        product_material = ProductMaterial.objects.all()
        serializer = ProductMaterialSerializer(product_material, many=True)
        return Response({"Product-Materiallar ro'yxati: ":serializer.data})


class WarehouseListApiView(APIView):
    '''Omborxonadagi barcha maxlulotlarni oluvchi API'''
    def get(self,request):
        warehouse = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouse, many=True)
        return Response ({"Omborxonadagi xomashyolar: ":serializer.data})



class ProductMaterialList(APIView):
    '''Berilgan shartlarni olish uchun umumiy ma'lumotlarni oluvchi API'''
    def get(self, request):
        products = Product.objects.all()
        result = []
        for product in products:
            product_data = {
                'product_name': product.product_name,
                'product_qty': product.product_quantity
            }
            materials = ProductMaterial.objects.filter(product=product)
            material_list = []
            for material in materials:
                warehouse = Warehouse.objects.filter(material=material.material).first()
                material_data = {
                    'warehouse_id': warehouse.id if warehouse else None,
                    'material_name': material.material.material_name,
                    'qty': material.quantity,
                    'price': warehouse.price if warehouse else None
                }
                material_list.append(material_data)
            product_data['product_materials'] = material_list
            result.append(product_data)
        return Response({'result': result})