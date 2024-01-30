import uuid
import base64

# Função para encurtar UUID para Base64
def encurtar_uuid_base64(uuid_str):
    uuid_bytes = uuid.UUID(uuid_str).bytes
    base64_encoded = base64.urlsafe_b64encode(uuid_bytes).decode().rstrip('=')
    return base64_encoded

# Exemplo de uso para o projeto "Projeto 1"
uuid_nomedoprojeto = str(uuid.uuid4())
uuid_encurtado_nomedoprojeto = encurtar_uuid_base64(uuid_nomedoprojeto)
print("Projeto 1 - UUID Original:", uuid_nomedoprojeto)
print("Projeto 1 - UUID Encurtado:", uuid_encurtado_nomedoprojeto)

# Exemplo de uso para o projeto "Projeto 2"
uuid_nomedoprojeto2 = str(uuid.uuid4())
uuid_encurtado_nomedoprojeto2 = encurtar_uuid_base64(uuid_nomedoprojeto2)
print("\nProjeto 2 - UUID Original:", uuid_nomedoprojeto2)
print("Projeto 2 - UUID Encurtado:", uuid_encurtado_nomedoprojeto2)

# Você pode adicionar mais projetos para gerar códigos
