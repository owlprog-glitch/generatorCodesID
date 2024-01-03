import uuid

def gerar_identificador_projeto(prefixo):
    # Gera um UUID versão 4 (baseado em números aleatórios)
    identificador = uuid.uuid4()

    # Converte o UUID para uma string e adiciona o prefixo
    identificador_str = f"{prefixo}_{str(identificador)}"

    return identificador_str

# Exemplo de uso para o projeto "Emergencia"
identificador_emergencia = gerar_identificador_projeto("EMR")
print("Identificador para Emergencia:", identificador_emergencia)

# Exemplo de uso para o projeto "HealthUnit"
identificador_healthunit = gerar_identificador_projeto("HU")
print("Identificador para HealthUnit:", identificador_healthunit)
