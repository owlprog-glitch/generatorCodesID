import random

class DocumentVersion:
    def __init__(self, project_name="Projeto"):
        self.project_name = project_name
        self.major = random.randint(0, 9)
        self.minor = random.randint(0, 9)
        self.patch = random.randint(0, 9)
        self.build = random.randint(0, 9)

    def __str__(self):
        return f"{self.project_name} - {self.major:02d}.{self.minor:02d}.{self.patch:02d}.{self.build:02d}"

# Exemplo de instância sem fornecer um nome de projeto, você pode utilizar como se fosse um Código de Cadastro para Documento (como desenhos daquele projeto, por exemplo)
versao_sem_projeto = DocumentVersion()
print("Versão sem projeto:", versao_sem_projeto)

# Exemplo de instância fornecendo um nome de projeto
versao_com_projeto = DocumentVersion("MeuProjeto")
print("Versão com projeto:", versao_com_projeto)
