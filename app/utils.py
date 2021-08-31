from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest
from .paypal import PayPalClient


class GetOrder(PayPalClient):
    """Transaction Dealils
        Detalles de la orden generada y antes de ser aprobada/completada
        :PayPalClient, clase definida con los datos de la cuenta de paypal
    """
    def get_order(self, order_id):

        request = OrdersGetRequest(order_id)
        response = self.client.execute(request)
        return response


class CaptureOrder(PayPalClient):
    """Capture Transaction
        
        Datos del pedido aprobado y finalizado
        :PayPalClient, clase definida con los datos de la cuenta de paypal
    """
    
    def capture_order(self, order_id, debug=False):
        
        request = OrdersCaptureRequest(order_id)
        response = self.client.execute(request)
        return response