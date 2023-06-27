from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver


#since category of products and order are common we created a list
Category =(  
    ('stationary','Stationary'),
    ('Vegetables','Vegetables'),
    ('Drinks','Drinks'),
    ('Fruits','Fruits'),
    ('Cereals','Cereals'),
)

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100,null=True) #Change it to choice later
    category = models.CharField(max_length=100,choices=Category,null=True)
    quantity = models.PositiveIntegerField(null=True)
    cost_per_item = models.DecimalField(max_digits=5,decimal_places=2,null=True)

#what are these for
    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    #since an order must be deleted when the product is deleted it's cascaded
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    #since an order must be deleted when the user is deleted it's cascaded
    staff = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    @property
    def sale(self):
        return self.order_quantity * self.product.cost_per_item

    def __str__(self):
        return f'{self.product.name}-{self.order_quantity}'
    
    def clean(self):
        q=self.product.quantity
        if self.order_quantity > self.product.quantity:
         raise ValidationError(('Available quantity is %(max_value)s.'), params={'max_value': self.product.quantity})
    
    