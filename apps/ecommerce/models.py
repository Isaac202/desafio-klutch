from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    price = models.FloatField(blank=False)
    quantity = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_id = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class OrderProduct(models.Model):
    order_id = models.IntegerField(blank=False)
    product_name = models.CharField(max_length=255, blank=False)
    quantity = models.IntegerField(blank=False)
    total = models.FloatField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)