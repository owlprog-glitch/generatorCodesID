import hashlib

def gerar_hash_projeto(texto):
    # Cria um objeto de hash SHA-256
    sha256 = hashlib.sha256()

    # Atualiza o objeto de hash com o texto codificado em bytes
    sha256.update(texto.encode('utf-8'))

    # Obtém o valor hexadecimal do hash
    hash_resultado = sha256.hexdigest()

    return hash_resultado

# Exemplo de uso para o projeto "nomedoprojeto"
texto_nomedoprojeto = "Dados relevantes do projeto XXXX"
hash_nomedoprojeto = gerar_hash_projeto(texto_XXXX)
print("Hash para nomedoprojeto:", hash_nomedoprojeto)

# Exemplo de uso para o projeto "nomedoprojeto2"
texto_nomedoprojeto2 = "Dados relevantes do projeto XXXX2"
hash_nomedoprojeto2 = gerar_hash_projeto(texto_XXXX2)
print("Hash para nomedoprojeto:", hash_nomedoprojeto2)
