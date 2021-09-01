# paypal-django
Integración de paypal con django y registro de transacción en DBA

# Observaciones
**Se recomienda seguir los siguientes pasos:**

1. *Instalar las siguientes librerías:* <br>

      pip install Django <br>
      pip install paypalrestsdk 

2. *Crear cuenta Sandbox-Paypal:*<br>

      [Crear cuenta](https://developer.paypal.com/docs/api/rest-sdks/ "Link")
  
 
3. *Modificar el archivo templates/index.html*
`Html`
``` [language]
 <!--Importante sustituir CLIENT_ID generando en su cuenta de paypal sandbox-->
 <script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID">
```

4. *Modificar el archivo app/paypal.py*
`Python`
``` [language]
  "Generar los datos desde la cuenta de paypal"    
   self.client_id="client_id"
   self.client_secret="client_secre
```

# PayPal

> [PayPal REST SDK](https://github.com/paypal/PayPal-Python-SDK "Link")

