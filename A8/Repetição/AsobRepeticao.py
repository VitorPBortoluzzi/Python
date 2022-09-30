#Digite o nome completo:

#A  Variavel de controne(inicio)
#B  Variavel de controle(Fim)
#C  Uso da variavel de controle na condição de parada/continue

# nome_completo = input("Digite seu nome completo: ")
# lista_de_nomes = nome_completo.split(" ")
# print("Voce digitou", len(lista_de_nomes),"nomes")

# nome_email = input("Digite seu email: ")
# lista_de_emails = nome_email.split("@")
# print("Usuário", lista_de_emails[0],"dominio:",lista_de_emails[-1])

#Repetição para validação
# while(True):
#     nome_completo = input("Digite seu nome completo: ")
#     nome_completo = nome_completo.title()
#     lista_de_nomes = nome_completo.split(" ")
#     if len(lista_de_nomes) < 2:
#         print("Voce digitou um nome incompleto")
#     else:
#         break

#Validar data:
# while(True):
#     data = input("Digite uma data [dd/mm/aaaa]: ")
#     lista = data.split("/")
#     if len(data) != 10 or len(lista) != 3 or int(lista[0]) < 1 or int(lista [0]) > 31 or int(lista[1]) < 1 or int(lista [1]) > 12:
#         print("A data é invalida. Redigite")
#     else:
#         break
# print("Voce digitou: ", data)
# print(lista)
# # print("Dia: ",lista[0])
# # print("Mes: ",lista[1])
# # print("Ano: ",lista[2])

#Categoria de jogos:
#Cadastração de categorias com controle de duplicadas
import re


lista_categorias_jogos = []

while(True):
    categoria = input("Digite categorias de jogos ou SAIR para finalizar: ")
    categoria = categoria.upper()
    if categoria == "SAIR":
        break
    if (categoria in lista_categorias_jogos):
        print("Categoria ja cadastrada")
    else :
        lista_categorias_jogos.append(categoria)
    ##Ordenar pq sim
    lista_categorias_jogos.sort()

##Outra forma de repetição:
print("Categorias cadastradas: ")
for item in lista_categorias_jogos:
    print(item)
# for item in range(0,len(lista_categorias_jogos)):
#     print(lista_categorias_jogos[item])
