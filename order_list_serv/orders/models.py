from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0)
    adress = models.CharField(max_length=200)
    order_date = models.DateTimeField('date ordered' , auto_now_add=True)

    def __str__(self):
        return self.order_id
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products' , default=1)



    def __str__(self):
        return self.product_name

 