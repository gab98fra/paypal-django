import json
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.base import View
from .utils import GetOrder, CaptureOrder
from .models import ProductModel, OrderModel

class TemplatePayView(TemplateView):
    "Template de pago"

    template_name="index.html"
    

class PayView(View):
    """Transaccion de paypal
        get: solicitud manual de url 
        post: Orden de compra vía paypal a través de las dos clases de paypal importadas
    """
    
    def get(self, request, *args, **kwargs):
        
        return redirect("design:design")

    def post(self, request, *args, **kwargs):
        
        "IMPORTANTE crear un producto en el modelo ProductModel"
        try:
            product=ProductModel.objects.get(id=1)
        except:
            print("IMPORTANTE crear un producto en el modelo ProductModel")
            
        #Datos de la orden generada
        data=json.loads(request.body)
        order_id=data["orderID"]
            
        #Datos de la orden generada antes de ser aprobada/completada
        details=GetOrder().get_order(order_id)
        details_price=float(details.result.purchase_units[0].amount.value)

        if details_price == product.price:
        #Validación de precios con la DBA
    
            #Trasacción aprobada
            trx=CaptureOrder().capture_order(order_id, debug=True)
                    
            #Guardar en DBA
            order=OrderModel(
                    order_id=trx.result.id,
                    status=trx.result.status,
                    status_code=trx.status_code,
                    amount=trx.result.purchase_units[0].payments.captures[0].amount.value,
                    name=trx.result.payer.name.given_name,
                    last_name=trx.result.payer.name.surname,
                    email=trx.result.payer.email_address,
                    address=trx.result.purchase_units[0].shipping.address.address_line_1,
                    payer_id=trx.result.payer.payer_id,
                    reference_id=trx.result.purchase_units[0].reference_id,
                    admin_area_1=trx.result.purchase_units[0].shipping.address.admin_area_1,
                    postal_code=trx.result.purchase_units[0].shipping.address.postal_code,
                    country_code=trx.result.purchase_units[0].shipping.address.country_code,
                    id_captures=trx.result.purchase_units[0].payments.captures[0].id,
                    paypal_fee=trx.result.purchase_units[0].payments.captures[0].seller_receivable_breakdown.paypal_fee.value,
                    net_amount=trx.result.purchase_units[0].payments.captures[0].seller_receivable_breakdown.net_amount.value,
                    create_time=trx.result.purchase_units[0].payments.captures[0].create_time,
                    reference_id_customer=details.result.purchase_units[0].reference_id,
                    order_id_customer=details.result.id,
                    intent_customer=details.result.intent,
                    product=ProductModel.objects.get(id=1),
                    user=request.user
                    )
            order.save()

            #Respuesta JSON
            data={
                    "id":f"{trx.result.id}",
                    "status":True,
                    "message":"La transacción fue exitosa"
                    }
            return JsonResponse(data)
        else:
            data={  
                    "status":False,
                    "message": "No se pudo completar la transacción"
                    }
            return JsonResponse(data)        

