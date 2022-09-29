# ## Grupo B

# 1. Faça um Programa que leia dados glicêmicos de um arquivo .txt (dados um abaixo do outro) conforme o exemplo:

# 123@21/09/2021@8:12

# 89@22/09/2021@7:50
# ...


# Onde, antes do arroba é o valor da glicemia vericada, após o primeiro arroba é a data de verificação e depois do último arroba é a hora de verificação.

# O programa deve conter um Menu de operação, como o exemplo:

# Menu
# 1 - Carregar arquivo
# 2 - Listar dados glicêmicos
# 3 - Calcular e mostrar medidas centrais (média, menor e maior valor)
# 4 - Sair
# Opção: ____

# Contudo, o programa deve obrigatoriamente trabalhar com classe Glicemia(valor, data, hora), manipulação de listas e arquivos .txt.


#Pedir o arquivo
#Lista de dados glicemicos
#Elementos da lista devem ser da classe Glicemia
#Percorrer o arquivo e a cada linha lida, splitar pelo simbolo "@" em objetos Glicemia,
#adicionando na lista;
#Aplicar na lista as medidas centrais

#EXEMPLOS/TESTES_USADOS:
# uma_medida = Glicemia(515,"22/09/2022","21:00")
# print(uma_medida.alerta())
