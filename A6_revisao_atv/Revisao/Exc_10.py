class Time:
    def __init__(self,nome,cidade,cores_principais):
        self.nome = nome
        self.cidade = cidade
        self.cores_principais = cores_principais

time1 = Time('Inter','SM','Vermelho/Branco')

time1.nome()

times = []
times.append(time1)
times.append(Time('Grêmio','PA','Azul/Branco/Preto'))

