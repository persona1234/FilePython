lettere = {} # dizionario vuoto 

while True:
    parola = input("Inserisci una parola -->").lower() # input di una parola e converto la parola in minuscolo
    for i in parola: # per ogni lettera nella parola
        if i in lettere: #se la lettera è già presente nel dizionario
            lettere[i] +=1 #aggiungi al valore 1
        else: # se la lettera è nuova
            lettere[i] = 1 # aggiungi alla lettera il valore 1
    print(lettere) #stampa il dizionario
    lettere = {} # svuota il dizionario
        
