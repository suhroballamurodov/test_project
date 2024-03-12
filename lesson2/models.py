from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='Product name')
    product_quantity = models.CharField(max_length=200, verbose_name='Product quantity')

    def __str__(self):
        return self.product_name

class Material(models.Model):
    material_name = models.CharField(max_length=200, verbose_name='Material name')

    def __str__(self):
        return self.material_name
    

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Material')
    quantity = models.IntegerField(verbose_name='Quantity')

    def __str__(self):
        return f"{self.product}" 
    

class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Material')
    remainder = models.IntegerField(verbose_name='Remainder')
    price = models.IntegerField(verbose_name='Price')
    
    def __str__(self):
        return f"{self.material}"