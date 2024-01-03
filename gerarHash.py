import hashlib

def gerar_hash_projeto(texto):
    # Cria um objeto de hash SHA-256
    sha256 = hashlib.sha256()

    # Atualiza o objeto de hash com o texto codificado em bytes
    sha256.update(texto.encode('utf-8'))

    # Obtém o valor hexadecimal do hash
    hash_resultado = sha256.hexdigest()

    return hash_resultado

# Exemplo de uso para o projeto "Emergencia"
texto_emergencia = "Dados relevantes do projeto Emergencia"
hash_emergencia = gerar_hash_projeto(texto_emergencia)
print("Hash para Emergencia:", hash_emergencia)

# Exemplo de uso para o projeto "HealthUnit"
texto_healthunit = "Dados relevantes do projeto HealthUnit"
hash_healthunit = gerar_hash_projeto(texto_healthunit)
print("Hash para HealthUnit:", hash_healthunit)
