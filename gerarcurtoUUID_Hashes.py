import uuid
import hashlib

# Função para encurtar UUID usando SHA-256
def encurtar_uuid_hash(uuid_str, comprimento=8):
    hash_obj = hashlib.sha256(uuid_str.encode('utf-8'))
    hash_resultado = hash_obj.hexdigest()
    return hash_resultado[:comprimento]

# Exemplo de uso para o projeto "nomedoprojeto"
uuid_nomedoprojeto = str(uuid.uuid4())
uuid_encurtado_nomedoprojeto = encurtar_uuid_hash(uuid_nomedoprojeto)
print("Projeto nomedoprojeto - UUID Original:", uuid_nomedoprojeto)
print("Projeto nomedoprojeto - UUID Encurtado:", uuid_encurtado_nomedoprojeto)

# Exemplo de uso para o projeto "nomedoprojeto2"
uuid_nomedoprojeto2 = str(uuid.uuid4())
uuid_encurtado_nomedoprojeto2 = encurtar_uuid_hash(uuid_nomedoprojeto2)
print("\nProjeto nomedoprojeto2 - UUID Original:", uuid_nomedoprojeto2)
print("Projeto nomedoprojeto2 - UUID Encurtado:", uuid_encurtado_nomedoprojeto2)
