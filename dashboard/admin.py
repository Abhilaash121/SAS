from django.contrib import admin
from .models import Product,Order

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity','cost_per_item')
    list_filter=('category',)

class OrderAdmin(admin.ModelAdmin):
    list_display=('product','staff','get_cpi','order_quantity','sale','date')

    def get_cpi(self,obj):
        return obj.product.cost_per_item
    get_cpi.admin_order_field  = 'product'  
    get_cpi.short_description = 'Cost per item'  

admin.site.site_header = "Tech Market Dashboard"
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)