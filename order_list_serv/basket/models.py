from django.db import models
# Create your models here.
# basket/models.py

from django.db import models
from django.contrib.auth.models import User

# class theCustomer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.user.username


class BasketItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)

