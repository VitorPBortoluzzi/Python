n = int(input("Digite um valor negativo ou positivo: "))

if n > 0:
    print(f'{n} é positivo')
elif n==0:
    print(f'{n} é zero')
else:
    print(f'{n} é negativo')