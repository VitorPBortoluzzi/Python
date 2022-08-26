from io import RawIOBase
from os import listxattr
from re import template


# 1) faça um programa em python utilizando:
#     - implementacão e chamada de método pessoal
#     - números aleatórios 
#     - listas 
#     - ordenacao de listas
     
    # a) O programa deve interagir com o usuário solcitando:
    #      1) quantos números gostaria de gerar;
    #      2) qual a faixa dos números, ou seja, entre qual faixa, por exemplo, 0 e 400
    # b) Em seguida, o programa (via métodos), deve popular a lista com esses números e exibi-la na tela 
    # c) O próximo passo é descobrir o menor e o maior valor da lista, bem como a média dos números presentes na listxattr
    # d) Ao final, exibir: menor valor, maior valor, média dos valores 
    
    #for i in range(len(numeros_list)):
    #    if (maiorNumero < numeros_list[i]):
    #        maiorNumero = numeros_list[i]
    #   if(menorNumero > numeros_list[i]):
    #       menorNumero = numeros_list[i]

    # OBS.: Para descobrir o menor e o maior valores, usar ordenação (sort) e capturar o primeiro e o 
    # último valor 