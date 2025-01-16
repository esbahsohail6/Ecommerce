from django.db import models
import datetime


class Category(models.Model):
    Category_id=models.AutoField
    Category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.Category_name


class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    product_price=models.DecimalField(default=0, decimal_places=2, max_digits=10)
    product_category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=250, default="", blank=True, null=True)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

    
class Customer(models.Model):
    Customer_id=models.AutoField
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.First_name} {self.Last_name}'

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount= models.IntegerField(default=1)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111,)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111)

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=1)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    description = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
