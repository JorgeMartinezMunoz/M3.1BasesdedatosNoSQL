import requests

# Paso 1: Definir la URL base y el ID del registro que deseas modificar
url_base = "https://66b4e5489f9169621ea4c340.mockapi.io/api/v1/contactos"
registro_id = "1"  # Cambia este valor por el ID del registro que deseas modificar
url = f"{url_base}/{registro_id}"

# Paso 2: Definir los nuevos datos del registro (esto sobrescribirá el registro existente)
datos_actualizados = {
    "nombre": "John Doe Jr.",
    "email": "johnjr@example.com",
    "telefono": "555-9876"
}

# Paso 3: Hacer una solicitud PUT para actualizar el registro
response = requests.put(url, json=datos_actualizados)

# Paso 4: Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print("Registro modificado exitosamente.")
    print("Datos del registro modificado:")
    print(response.json())
else:
    print("Error al modificar el registro. Código de estado:", response.status_code)