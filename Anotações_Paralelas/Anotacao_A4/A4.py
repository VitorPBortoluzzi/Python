frase = input("Digite sua demanda: ")
print("Sua demanda é: "+frase)
frase = frase.upper()
if ((frase.find("QUERO") != -1) or (frase.find("PRECISO") != -1 )or (frase.find("NECESSITO")!= -1) or (frase.find("DEVO")!= -1)):
    print("Demanda de emergência")
elif(frase.find("RIA") != -1):
    print ("Demanda de urgencia mas com atenção")
else:
    print ("Relato sem demanda")