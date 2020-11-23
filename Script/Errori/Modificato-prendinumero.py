
try:
    numero = int(input("Inserisci un numero:"))

    if numero >0:
        print("Il numero è positivo")
        
    elif numero == 0:
        print("Il numero è zero")
        
    else:
        print("Il numero è negativo")
except:
    #pass lascia tutto com'è e termina il programma.
    print("Ho riscontrato un errore...")


