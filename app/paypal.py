import sys
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment

class PayPalClient:
    "Clase padre: Datos de la cuenta de paypal"
    
    def __init__(self):

        "Generar los datos desde la cuenta de paypal"    
        self.client_id="client_id"
        self.client_secret="client_secret"

        """Configure y devuelva PayPal entorno del SDK de Python con credenciales de acceso PayPal.
           Para test utilizar SandboxEnvironment. En producción utilizar LiveEnvironment."""
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)

        """ Devuelve PayPal instancia de cliente HTTP con un entorno que tiene acceso contexto de credenciales. 
            Utilice esta instancia para invocar PayPal API, 
            siempre que el las credenciales tienen acceso. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Función para imprimir todos los datos json de una manera legible y organizada
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key,value in itr:
            # Omitir atributos internos.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                        self.object_to_json(value) if not self.is_primittive(value) else\
                         value
        return result

    def array_to_json_array(self, json_array):
        result =[]
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if  not self.is_primittive(item) \
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)  

