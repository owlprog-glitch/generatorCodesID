import uuid

def gerar_identificador_projeto(prefixo):
    # Gera um UUID versão 4 (baseado em números aleatórios)
    identificador = uuid.uuid4()

    # Converte o UUID para uma string e adiciona o prefixo
    identificador_str = f"{prefixo}_{str(identificador)}"

    return identificador_str

# Exemplo de uso para o projeto "nomedoprojeto"
identificador_nomedoprojeto = gerar_identificador_projeto("EMR")
print("Identificador para nomedoprojeto:", identificador_nomedoprojeto)

# Exemplo de uso para o projeto "nomedoprojeto2"
identificador_nomedoprojeto2 = gerar_identificador_projeto("HU")
print("Identificador para nomedoprojeto2:", identificador_nomedoprojeto2)

# Pode ser adicionado mais, veja o exemplo das letras "EMR" e "HU"
