import random
import statistics

numeros_list = []
x = int (input("Digite a quantidade de numeros a serem gerados: "))
print("Digite o intervalo de numeros")
faixaIni = int (input("Inicial: "))
faixaFim = int (input("Final: "))

for i in range(0,x):
    n = random.randint(faixaIni,faixaFim)
    numeros_list.append(n)

print(numeros_list)
numeros_list.sort()

maiorNumero = 0
menorNumero = faixaFim + 1
maiorNumero = numeros_list[-1]
menorNumero = numeros_list[0]

print(menorNumero)
print(maiorNumero)
print(statistics.mean(numeros_list))