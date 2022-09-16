vogais = ['A','E','I','O','U','a','e','i','o','u']

Caracter = input("Digite uma letra: ")

if Caracter.isalpha()== True:
    if(Caracter in vogais):
        print("Voce digitou uma vogal")
    else:
        print("voce digitou uma consoante")
else:
    print("Voce digitou um caracter diferente de letras")

#if(Caracter in vogais):
#    print("Voce digitou uma vogal")
#else:
#    print("voce digitou uma consoante")
