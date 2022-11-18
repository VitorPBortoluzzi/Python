from __future__ import with_statement
from asyncio.windows_events import NULL
from audioop import reverse

class Palavra:
    valor = ""
    quantidade = 0

    def __init__(self, valor):
        self.valor = valor
        self.quantidade = 1

    def __eq__(self, other):
        if isinstance(other, Palavra):
            return self.valor == other.valor
        return False
    
    def __gt__(self, other):
        if self.quantidade == other.quantidade:
            return self.valor < other.valor
        return self.quantidade > other.quantidade
####################################################################
lista_palavras = []
nome_arquivo = ""
lista_vezes_palavra = []
vezes = 0
####################################################################
class Util:
    @staticmethod
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
                    dados_linha = linha.split(" ")
                    for palavra in dados_linha:
                        palavra = palavra.lower()
                        palavra = palavra.replace(".","")
                        palavra = palavra.replace(",","")
                        palavra = palavra.replace(";","")
                        palavra = palavra.replace("!","")
                        palavra = palavra.replace("?","")
                        palavra = palavra.replace("<","")
                        palavra = palavra.replace(">","")
                        palavra = palavra.replace("\n","")

                        palavra_obj = Palavra(palavra)
                        encontrado = False
                        for p in lista_palavras:
                            if(p.valor == palavra_obj.valor):
                                p.quantidade += 1
                                encontrado = True
                        if (not encontrado):
                            lista_palavras.append(palavra_obj)
        except:
            print("Erro")

    def exibir_lista_palavras(lista_palavras):
        for palavra in lista_palavras:
            print(palavra.valor, " - ", palavra.quantidade)
    
    def vezesQ_aparece(lista_vezes_palavra,nome_arquivo):
        try:
            with open(nome_arquivo,'r', encoding="utf8") as leitor:
                for linha in leitor:
                    dados_linha = linha.split(" ")
                    for palavra in dados_linha:
                        palavra = palavra.lower()
                        palavra = palavra.replace(".","")
                        palavra = palavra.replace(",","")
                        palavra = palavra.replace(";","")
                        palavra = palavra.replace("!","")
                        palavra = palavra.replace("?","")
                        palavra = palavra.replace("<","")
                        palavra = palavra.replace(">","")
                        palavra = palavra.replace("\n","")
                        lista_vezes_palavra.append(palavra)
        except:
            print("Erro")
        vezes = lista_vezes_palavra.count(temp)
        print(temp.title(),"aparece:",vezes)


while(True):
    print("MENU"    )
    print("1- Carregar arquivo texto")
    print("2 - Exibir palavras/ocorrencias")
    print("3 - Vezes q aparece <x> ")
    print("4 - Sair")
    opcao = int(input("Opção:"))

    if(opcao == 1):
        print("Abrindo o arquivo.....")
        nome_arquivo = Util.abrir_arquivo_texto()
        pass
    elif(opcao ==2):
        lista_palavras.clear()
        print("Lista de palavras....")
        Util.criar_lista_palavras(lista_palavras,nome_arquivo)
        lista_palavras.sort(reverse = True)
        Util.exibir_lista_palavras(lista_palavras)
    elif(opcao == 3):
        lista_vezes_palavra.clear()
        nome_arquivo = Util.abrir_arquivo_texto()
        temp = input("Palavra/expressão: ")
        Util.vezesQ_aparece(lista_vezes_palavra,nome_arquivo)
        

    elif(opcao == 4):
        break
    else:
        print("Opção invalida")
