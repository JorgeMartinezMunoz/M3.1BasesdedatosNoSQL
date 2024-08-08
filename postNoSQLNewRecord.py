import requests

# Paso 1: Definir la URL base
url = "https://66b4e5489f9169621ea4c340.mockapi.io/api/v1/contactos"

# Paso 2: Definir los datos del nuevo registro
nuevo_registro = {
    "nombre": "Jorge Mtz",
    "email": "jane@example.com",
    "telefono": "555-5678"
}

# Paso 3: Hacer una solicitud POST para agregar el nuevo registro
response = requests.post(url, json=nuevo_registro)

# Paso 4: Verificar si la solicitud fue exitosa
if response.status_code == 201:  # 201 Created es el código de éxito para creación de recursos
    print("Registro agregado exitosamente.")
    print("Datos del nuevo registro:")
    print(response.json())
else:
    print("Error al agregar el registro. Código de estado:", response.status_code)
