import uuid
import base64

# Função para encurtar UUID para Base64
def encurtar_uuid_base64(uuid_str):
    uuid_bytes = uuid.UUID(uuid_str).bytes
    base64_encoded = base64.urlsafe_b64encode(uuid_bytes).decode().rstrip('=')
    return base64_encoded

# Exemplo de uso para o projeto "Emergencia"
uuid_emergencia = str(uuid.uuid4())
uuid_encurtado_emergencia = encurtar_uuid_base64(uuid_emergencia)
print("Projeto Emergencia - UUID Original:", uuid_emergencia)
print("Projeto Emergencia - UUID Encurtado:", uuid_encurtado_emergencia)

# Exemplo de uso para o projeto "HealthUnit"
uuid_healthunit = str(uuid.uuid4())
uuid_encurtado_healthunit = encurtar_uuid_base64(uuid_healthunit)
print("\nProjeto HealthUnit - UUID Original:", uuid_healthunit)
print("Projeto HealthUnit - UUID Encurtado:", uuid_encurtado_healthunit)