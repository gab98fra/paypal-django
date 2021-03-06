# paypal-django
Integración de paypal con django y registro de transacción en DBA

# Recomendaciones
**Se recomienda seguir los siguientes pasos:**

1. *Instalar las siguientes librerías:* <br>

  ``` [language]
  pip install Django, paypalrestsdk
  ```

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
* Nota. Crear al menos un producto, implementar login o al menos estar logeado en admin en caso contrario es posible que le arroje un error por csrf token.

# PayPal

> [PayPal REST SDK](https://github.com/paypal/PayPal-Python-SDK "Link")

