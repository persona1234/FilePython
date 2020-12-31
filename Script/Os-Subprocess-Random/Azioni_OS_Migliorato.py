# Ho spostato lo script in una cartella con altri file.
# Lo scopo del programma sarà: trovare il percorso, il nome dei file,
# verificare l'estensione dei file in modo da colpire solo i file .txt
# rinominare suddetti file e creare un file .txt con la lista dei file.
# Per la scrittura del file si può utilizzare anche os ma noi utilizziamo il metodo che sappiamo usare.

import os

percorso = os.getcwd()
print(percorso)
conta = 0
conta_finale =  0
file_finale = open("Lista_file.txt","w") # Creo il file
file_finale.write("File colpiti:\n") # Scrivo la riga e vado a capo

for cartelle,sottocartelle,files in os.walk(percorso):
  
    for file in files:
        conta += 1
        print(file)
        print(conta)
        if file.endswith(".txt"):
            print("Si")
            try: # prova, potrebbero sorgere delle eccezione
                conta_finale += 1
                nuovo_nome = "Ciao "+file
                os.rename(file,nuovo_nome)
                stringa_da_scrivere = (file,"--->",nuovo_nome) # Questa è una tuple
                stringa_da_scrivere = str(stringa_da_scrivere)
                file_finale.write(stringa_da_scrivere+"\n")
            except: # Se fallisce continua
                conta_finale -= 1
                pass
        else:
            print(file)
    print(f"I file totali sono: {conta}, i file colpiti sono: {conta_finale}")

        
