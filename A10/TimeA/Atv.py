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
from encodings import utf_8
from operator import truediv

import os

class Pessoa:
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

def valida_nome(nome):
    nomes = nome.split(" ")
    if len(nomes) <= 1:
        return False
    else:
        return True

def valida_email(email):
    if (not email.__contains__('@') or not email.__contains__('.com')):
        return False
    else:
        return True
        
def jaCadastrado(matricula, lista):
    for pessoa in lista:
        if(matricula == pessoa.matricula):
            return True
        return False

lista_Inscricao = []
arq_inscritos = "Inscritos.csv"
try:
    with open(arq_inscritos, "r", encoding='utf8') as procurador:
        for linha in procurador:
            dados_linha = linha.split(';')
            pessoa = Pessoa(dados_linha[0],dados_linha[1],dados_linha[2])
            lista_Inscricao.append(pessoa)
except:
    pass

while(True):
    print("Menu")
    print("1 - Registrar inscrição")
    print("2 - Listar Inscritos")
    print("3 - Registrar Presença")
    print("4 - Lista de Presença")
    print("5 - Sair")
    opcao = int(input("Opção: "))
    
    if(opcao == 1):
        # nome = input("Nome: ")
        # email = input("Email: ")
        # matricula = input("Matricula: ")
        # arq_inscritos = open("Inscritos.csv", "a")
        # arq_inscritos.write(nome + ";" + email + ";" + matricula + ".\n" )
        # arq_inscritos.close()
        while (True):
            nome = input("Insira o nome completo:")
            if (valida_nome(nome) == True):
                break
            else:
                print("Siga as instruções")
        while (True):
            email = input ("Digite o email:")
            if len(email) > 10:
                if(valida_email(email) == True):
                    break
                else:
                    print("exemplo@plataforma.com")
        while (True):
            matricula = input("Insira a matricula: ")
            if len(matricula) >= 5:
                break
        pessoa = Pessoa(nome,email,matricula)
        
        if(jaCadastrado(matricula,lista_Inscricao)):
            print("Essa pessoa já esta cadastrada")
        
        else:lista_Inscricao.append(pessoa)

        try:
            with open(arq_inscritos, "a", encoding='utf8') as procurador:
                procurador.write(nome + ";" + email + ";" + matricula + "." + "\n")
                procurador.close()
        except:
            pass
    elif(opcao==2):
        print("Listagem de incritos: ")
        for pessoa in lista_Inscricao:
            print("Matricula:" + pessoa.matricula + "" + "Nome:" +pessoa.nome + ".\n")
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