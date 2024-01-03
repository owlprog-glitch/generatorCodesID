import uuid
import hashlib

# Função para encurtar UUID usando SHA-256
def encurtar_uuid_hash(uuid_str, comprimento=8):
    hash_obj = hashlib.sha256(uuid_str.encode('utf-8'))
    hash_resultado = hash_obj.hexdigest()
    return hash_resultado[:comprimento]

# Exemplo de uso para o projeto "Emergencia"
uuid_emergencia = str(uuid.uuid4())
uuid_encurtado_emergencia = encurtar_uuid_hash(uuid_emergencia)
print("Projeto Emergencia - UUID Original:", uuid_emergencia)
print("Projeto Emergencia - UUID Encurtado:", uuid_encurtado_emergencia)

# Exemplo de uso para o projeto "HealthUnit"
uuid_healthunit = str(uuid.uuid4())
uuid_encurtado_healthunit = encurtar_uuid_hash(uuid_healthunit)
print("\nProjeto HealthUnit - UUID Original:", uuid_healthunit)
print("Projeto HealthUnit - UUID Encurtado:", uuid_encurtado_healthunit)
