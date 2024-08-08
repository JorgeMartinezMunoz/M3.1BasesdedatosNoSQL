import requests

# Paso 1: Definir la URL base y el ID del registro que deseas eliminar
url_base = "https://66b4e5489f9169621ea4c340.mockapi.io/api/v1/contactos"
registro_id = "1"  # Cambia este valor por el ID del registro que deseas eliminar
url = f"{url_base}/{registro_id}"

# Paso 2: Hacer una solicitud DELETE para eliminar el registro
response = requests.delete(url)

# Paso 3: Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print(f"Registro con ID {registro_id} eliminado exitosamente.")
else:
    print(f"Error al eliminar el registro. Código de estado: {response.status_code}")