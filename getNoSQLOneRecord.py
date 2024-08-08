import requests

# Paso 1: Definir la URL base y el ID del registro que quieres consultar
url_base = "https://66b4e5489f9169621ea4c340.mockapi.io/api/v1/contactos"
registro_id = "1"  # Cambia este valor por el ID del registro que deseas consultar
url = f"{url_base}/{registro_id}"

# Paso 2: Hacer una solicitud GET a la URL del registro específico
response = requests.get(url)

# Paso 3: Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()

    # Paso 4: Mostrar todos los campos del registro en formato plano
    print("Datos del registro en formato plano:")
    for key, value in data.items():
        print(f"{key}: {value}")

else:
    print("Error al realizar la solicitud. Código de estado:", response.status_code)