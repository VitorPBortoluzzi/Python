#Elementos da lista devem ser da classe Glicemia
class Glicemia:
    valor_glicemia = 0
    data_medicao = ""
    hora_medicao = ""

    def __init__(self,valor_glicemia,data_medicao,hora_medicao):
        self.valor_glicemia = valor_glicemia
        self.data_medicao = data_medicao
        self.hora_medicao = hora_medicao

    def alerta(self):
        if self.valor_glicemia < 70:
            return "Atenção entrando em HIPOGLICEMIA"
        elif self.valor_glicemia > 180:
            return "Atenção indice glicemico MUITO ALTO, HIPERGLICEMIA"
        else:
            return "Glicemia normal"


#Pedir o arquivo
nome_arquivo = input("Insira o nome do Arquivo: ")

#Lista de dados glicemicos
lista_glicemica = []

#Percorrer o arquivo e a cada linha lida, splitar pelo simbolo "@" em objetos Glicemia,
#adicionando na lista;
procurador_arquivo = open(nome_arquivo,"r")

for linha in procurador_arquivo:
    dados_linha = linha.split("@")
    lista_glicemica.append(Glicemia(dados_linha[0],dados_linha[1],dados_linha[2]))
    print(linha)
#Aplicar na lista as medidas centrais


procurador_arquivo.close()