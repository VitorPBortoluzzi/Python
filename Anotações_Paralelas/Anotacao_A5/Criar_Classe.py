## Cria o objeto e insere após os dados
class Glicemia:
    valor = 0
    data = " "
    hora = " "

Objeto_1 = Glicemia() #Invocando Classe --> Contrutor: Mesmo nome da classe.Ele instancia objetos no programa
Objeto_1.valor = 194
Objeto_1.data = "1/09/2022"
Objeto_1.hora = "21:00"


## Construtor = __init_
#Cria o objeto e já insere
class Glicemia:
    def __init__(Self,valor,data,hora):
        Self.valor=valor
        Self.data=data
        Self.hora=hora

Objeto_1 = Glicemia(194,"01/09/2022","21:00")

class Aluno:
    nome = ""
    curso = ""
    def pegar_Sobrenome(Self):
        nomes = Self.nome.split()
        return nomes[-1]


Um_aluno = Aluno()
Um_aluno.nome = "Vitor Bortoluzzi"
Um_aluno.curso = "CC"

#print(Um_aluno.pegar_Sobrenome())

class AlunoInit:
    def __init__(Self,nome,curso):
        Self.nome = nome
        Self.curso = curso

    def pegar_Sobrenome(Self):
        nomes = Self.nome.split()
        return nomes[-1]
Um_aluno = AlunoInit("Vitor Bortoluzzi", "CC")

#print(Um_aluno.pegar_Sobrenome())

class AlunoZam:
    def __init__(Self,nome,curso):
        Self.nome = nome
        Self.curso = curso

    def pegar_Sobrenome(Self):
        nomes = Self.nome.split()
        return nomes[-1]
    #toString
    def __Str__ (Self):
        return "Nome:"+Self.nome + "Cruso: " + Self.curso


aluno_1 = AlunoZam("Jonatham","SI")
print(aluno_1)
# imprime local da memória
#===========
#pós toString
aluno_2 = AlunoZam("Jonatham","SI")
print(aluno_2.__Str__())
