class Produto:
    descricao = ""
    valor = 0
    
    def __init__(self, descricao, valor): 
        self.descricao = descricao
        self.valor = valor

    def details(self):
        print (f'Descrição:{self.descricao}')
        print (f'Valor:{self.valor}\n')
        

p1 = Produto("Arroz",100)
p2 = Produto("Feijão",50)
p1.details()
p2.details()