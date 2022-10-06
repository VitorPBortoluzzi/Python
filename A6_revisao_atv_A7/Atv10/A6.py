#Elementos da lista devem ser da classe Glicemia
class Glicemia:

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
nome_arquivo = input("Insira o nome do Arquivo:")

#Lista de dados glicemicos
lista_glicemica = []

#Percorrer o arquivo e a cada linha lida, splitar pelo simbolo "@" em objetos Glicemia,
#adicionando na lista;
try:
    with open(nome_arquivo,'r') as procurador:
        for linha in procurador:
            dados_linha = linha.split("@")
            lista_glicemica.append(Glicemia(int(dados_linha[0]),dados_linha[1],dados_linha[2]))
except:
    print("Porblema com arquivo")

for item in lista_glicemica:
    print(item.valor_glicemia)
#Aplicar na lista as medidas centrais

soma = 0
for item in lista_glicemica:
    soma = soma + item.valor_glicemia

media = soma / len(lista_glicemica)
print("A média glicemica é: ",round(media,1))


menor_glicemia = min(lista_glicemica, key = lambda g : g.valor_glicemia)
print("O menor valor é: ",menor_glicemia.valor_glicemia," ",menor_glicemia.data_medicao)

maior_glicemia = max(lista_glicemica, key= lambda g: g.valor_glicemia)
print("O maior valor é: ",maior_glicemia.valor_glicemia," ",maior_glicemia.data_medicao)