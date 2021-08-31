from django.contrib import admin
from .models import ProductModel, OrderModel


class OrderAdmin(admin.ModelAdmin):
    """Funcionalidades
        -Buscador
        -Campos visualizados en el dashboard
    """    
    search_fields=['email']
    list_display=("order_id", "user","email","create_time", "created")
    

admin.site.register(ProductModel)
admin.site.register(OrderModel, OrderAdmin)