from __future__ import with_statement
class palavra:
    valor = ""
    quantidade = 0

    def __init__(self,valor):
        self.valor = valor.lower()
        self.quantidade = 1

lista_palavras = []
nome_arquivo = ""
####################################################################
def abrir_arquivo_texto():
    nome_arquivo = input("Digite caminho e/ou nome do arquivo texto:")
    try:
        with open(nome_arquivo,'r', encoding="utf8") as leitor:
            for linha in leitor:
                print(linha)
    except:
        print("Arquivo não encontrado ou com problema")
    return(nome_arquivo)

def criar_lista_palavras(lista_palavras,nome_arquivo):
    try:
        with open(nome_arquivo,'r', encoding="utf8") as leitor:
            for linha in leitor:
                dados_linha = linha.split(" " and ".")
                for palavra in dados_linha:
                    palavra = palavra.lower()
                    lista_palavras.append(palavra)
    except:
        print("Erro")

def exibir_lista_palavras(lista_palavras):
    for palavra in lista_palavras:
        print(palavra)

lista_palavras = []
while(True):
    print("MENU"    )
    print("1- Carregar arquivo texto")
    print("2 - Exibir palavras/ocorrencias")
    print("4 - Sair")
    opcao = int(input("Opção:"))

    if(opcao == 1):
        print("Abrindo o arquivo.....")
        nome_arquivo = abrir_arquivo_texto()
        pass
    elif(opcao ==2):
        lista_palavras.clear()
        print("Lista de palavras....")
        criar_lista_palavras(lista_palavras,nome_arquivo)
        exibir_lista_palavras(lista_palavras)

    elif(opcao == 4):
        break
    else:
        print("Opção invalida")
