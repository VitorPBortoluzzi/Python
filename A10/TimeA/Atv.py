# Arquivo
#     -Leitura
#     -Escrita

# Menu
#     1 Registrar inscrição:
#         Classe pessoa:
#             nome Completo
#             email
#             matricula
from __future__ import with_statement

class pessoa:
    def __init__(self,nome,email,matricula):
        self.nome = nome
        self.email = email
        self.matricula = matricula

    def primeiro_nome(self):
        nomes = self.nome.split(" ")
        return nomes[0]

    def sobre_nome(self):
        nomes = self.nome.split(" ")
        return nomes[-1]

lista_Inscricao = []

while(True):
    print("Menu")
    print("1 - Registrar inscrição")
    print("2 - Listar Inscritos")
    print("3 - Registrar Presença")
    print("4 - Lista de Presença")
    print("5 - Sair")
    opcao = int(input("Opção: "))
    
    if(opcao == 1):
        nome = input("Nome: ")
        email = input("Email: ")
        matricula = input("Matricula: ")
        arq_inscritos = open("Inscritos.csv", "a")
        arq_inscritos.write(nome + ";" + email + ";" + matricula + ".\n" )
        arq_inscritos.close()


    elif(opcao == 5):
        break
#         Arquivos
#         Inscritos.csv        |  Presenca.csv
#         nome;email;matricula |  Matricula;data/hora
#     2 Listar incritos
#     3 Registrar Presença
#     4 Listar Presença : 
#         Matricula & nome
#     5 Sair

# Opção: