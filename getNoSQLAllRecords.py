import requests
import pandas as pd
import json

# Paso 1: Hacer una solicitud GET a la URL
url = "https://66b4e5489f9169621ea4c340.mockapi.io/api/v1/contactos"
response = requests.get(url)

# Paso 2: Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()

    # Paso 3: Mostrar los datos en formato JSON formateado
    print("Datos en formato JSON formateado:")
    print(json.dumps(data, indent=4))

    # Paso 4: Convertir los datos a un DataFrame de pandas
    df = pd.DataFrame(data)

    # Mostrar el DataFrame
    print("\nDatos en formato DataFrame:")
    print(df)

    # Paso 5: Exportar el DataFrame a un archivo CSV
    df.to_csv('contactos.csv', index=False)
    print("\nEl DataFrame ha sido exportado a 'contactos.csv'.")
else:
    print("Error al realizar la solicitud. Código de estado:", response.status_code)