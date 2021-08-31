from django.db import models
from django.contrib.auth.models import User

class ProductModel(models.Model):
    product=models.CharField(max_length=100, blank=True, null=True)
    price=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.product

class OrderModel(models.Model):
    "Compra realizada"

    id=models.BigAutoField(primary_key=True)
    order_id=models.CharField(max_length=50, blank=True, null=True)
    status=models.CharField(max_length=50, blank=True, null=True)
    status_code=models.IntegerField(blank=True, null=True)
    amount=models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    name=models.CharField(max_length=100, blank=True, null=True)
    last_name=models.CharField(max_length=100, blank=True, null=True)
    email=models.EmailField(max_length=100, blank=True, null=True)
    address=models.CharField(max_length=100, blank=True, null=True)
    payer_id=models.CharField(max_length=50, blank=True, null=True)
    reference_id=models.CharField(max_length=50, blank=True, null=True)
    admin_area_1=models.CharField(max_length=100, blank=True, null=True)
    postal_code=models.IntegerField(blank=True, null=True)
    country_code=models.CharField(max_length=20, blank=True, null=True)
    id_captures=models.CharField(max_length=50, blank=True, null=True)
    paypal_fee=models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    net_amount=models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    reference_id_customer=models.CharField(max_length=50, blank=True, null=True)
    order_id_customer=models.CharField(max_length=50, blank=True, null=True)
    intent_customer=models.CharField(max_length=50, blank=True, null=True)
    create_time=models.CharField(max_length=50, blank=True, null=True)
    product=models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created=models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ["created"]
        verbose_name = "Venta"    
        verbose_name = "Venta"    
    
    def __str__(self):
        return str(self.user)
     