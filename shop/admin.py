from django.contrib import admin

# Register your models here.
from .models import Product,Category,Order,Customer,Contact,OrderUpdate

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderUpdate)
admin.site.register(Customer)
admin.site.register(Contact)