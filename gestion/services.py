# gestion/services.py

import requests

LOGIN_SERVICE_URL = "http://127.0.0.1:8000/api/auth/users/"  # Ajusta si tu endpoint es diferente

def obtener_usuarios_no_admin():
    try:
        response = requests.get(LOGIN_SERVICE_URL)
        if response.status_code == 200:
            usuarios = response.json()
            # Filtrar por roles deseados
            return [u for u in usuarios if u.get("role") in ["jefe_brigada", "tecnico", "botanico"]]
        else:
            return []
    except Exception as e:
        print("Error consultando login-service:", e)
        return []
