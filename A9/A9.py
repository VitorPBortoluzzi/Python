#Correção desafio A8:Bibliografia Sobrenomes

#menu de opções para o usuario
# Menu
# 1 - Abrir arquivo bibliografico.
# 2 - Listar autores.
# 3 - Principal Autor
# 4 - Sair
# Opção

#Estruturas de dados /Ferramentas
# 1 - Classe do tipo Autor: nome, sobrenome, ocorrencias
# 2 - Lista []
# 3 - with open(nome_arquivo,'r') as procurador:
# 4 - Método Split()
from __future__ import with_statement
from codecs import latin_1_decode
class Autor:
    def __init__(self,nome,sobrenome,ocorrencias):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ocorrencias = ocorrencias

lista_autores = []

nome_arquivo = input("Insira o nome do Arquivo:")

while(True):
    print("MENU")
    print("1 - Abrir arquivo bibliográfico")
    print("2 - Lista Autores")
    print("3 - Principal Autor")
    print("4 - Sair")
    opcao = int(input("Opção: "))

    if (opcao == 1):
        print("Exibir a bibliografia:")
        try:
            with open(nome_arquivo,'r', encoding="utf8") as procurador:
                for linha in procurador:
                    if(not linha[0] == '#'):
                    # if (not linha.__contains__("#")):
                        print(linha)
        except:
            print("Porblemas com  o arquivo\n\t Ou Arquivo Inexistente")

    elif(opcao == 2):
        print("Exibindo Autores\n")
        try:
            with open(nome_arquivo,'r', encoding="utf8") as procurador:
                for linha in procurador:
                    if(not linha[0] == '#'):
                        dados_linha = linha.split(". ")
                        autores = dados_linha[0].split(".;")
                        for elemento in autores:
                            if (not elemento.strip in lista_autores):
                                lista_autores.append(elemento)
                for autor in lista_autores:
                    print(autor)
        except:
            print("Porblemas com  o arquivo\n\t Ou Arquivo Inexistente")
    elif(opcao == 3):
        print("Principal Autor\n")
    elif(opcao == 4):
        print("\tAté logo")
        break
    else:
        print("opcao invalida")