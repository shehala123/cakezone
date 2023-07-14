from django.db import models
from store.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(null=True)
    status=models.CharField(max_length=100,default="cart")
    
    @property
    def qtyprice(self):
        tot=self.product.price*self.quantity
        print(tot)
        return tot
    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    weight=models.CharField(max_length=50)
    # description=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    options=(
        ("order placed","order placed"),
        ("shipped","shipped"),
        ("out for delivery" ,"out for delivery"),
        ("delivered","delivered"),
        ("Cancel","Cancel")
    )
    status=models.CharField(max_length=100,choices=options,default="order placed")
    date=models.DateField(auto_now_add=True)
    
