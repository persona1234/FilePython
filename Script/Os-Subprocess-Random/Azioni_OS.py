import os # Importo os

percorso = os.getcwd() # Restituisce il percorso in cui il file è situato
print(percorso)

conta = 0  # creo una variabile con associato il valore 0
for cartelle,sottocartelle,files in os.walk(percorso):
    """
    Walk percorre tutti i file di una directory
    al porsto della solita i ho utilizzato cartellem,sottocartelle e files.
    Funziona allo stesso modo ma è più comodo per i percorsi in quanti li divide
    """
    for file in files: # Divido i file in modo da lavorare con essi 
        conta += 1 # Ad ogni file aggiungi il valore 1
        print(files) # Stampa i nomi dei file
        print(conta) # Stampa i numeri di file trovati
        
