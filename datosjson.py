import json
from datetime import datetime, timedelta

nombre_archivo = 'myfile.json'

try:
    # Abrir el archivo JSON para lectura
    with open(nombre_archivo, 'r') as json_file:
        # Cargar el contenido del archivo JSON en una variable
        ourjson = json.load(json_file)
        
        for obj in ourjson:
            # Acceder a los valores usando las claves del objeto
            token = obj['token']
            tiempo_expiracion = datetime.strptime(obj['expiry'], '%Y-%m-%dT%H:%M:%S.%fZ')
            tiempo_restante = tiempo_expiracion - datetime.utcnow()

        # Imprimir el valor del token
        print(f"El valor del token es: {token}")
        
        # Calcular cuánto tiempo queda antes de que caduque el token
        #tiempo_expiracion = datetime.strptime(ourjson['expiry'], '%Y-%m-%dT%H:%M:%S.%fZ')
        #tiempo_restante = tiempo_expiracion - datetime.utcnow()
        
        # Imprimir cuánto tiempo queda antes de que caduque el token
        print("Tiempo restante antes de que caduque el token:", tiempo_restante)
        
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se encontró.")
except json.JSONDecodeError:
    print(f"El archivo {nombre_archivo} no tiene un formato JSON válido.")
except KeyError as e:
    print(f"La clave {e} no se encuentra en el JSON.")
