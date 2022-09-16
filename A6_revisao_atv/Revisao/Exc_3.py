nome_completo = input("Digite seu nome completo: ")
nome_completo = nome_completo.upper()

#if "OLIVEIRA" in nome_completo:
if nome_completo.find('OLIVEIRA') == 1:
    print('Oliveira presente no nome')
else:
    print(f'Bem-vindo: {nome_completo}')