frase = input("Digite sua demanda: ")
print("Sua demanda é: "+frase)

if ((frase.find("quero") != -1) or (frase.find("preciso") != -1 )or (frase.find("necessito")!= -1) or (frase.find("devo")!= -1)):
    print("Demanda de emergência")
elif(frase.find("ria") != -1):
    print ("Demanda de urgencia mas com atenção")
else:
    print ("Relato sem demanda")