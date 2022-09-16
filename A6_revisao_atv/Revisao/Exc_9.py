class CEP:
    numero = 0
    cidade = ""
    estado = ""
#def __init.. = construtor
    def __init__(self,numero,cidade,estado):
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def pessoa(self):
        print (f'Numero:{self.numero}')
        print (f'Cidade:{self.cidade}')
        print (f'Numero:{self.estado}\n')

cep1 = CEP(97065090,'SM','RS')
cep2 = CEP(470,'SC','RS')
cep1.pessoa()
cep2.pessoa()
