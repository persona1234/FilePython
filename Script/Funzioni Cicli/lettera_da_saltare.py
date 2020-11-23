""" L'utente sceglie una lettera
Il ciclo analizza la stringa data e se presente salta la lettera .
"""
parola = "scarafaggio"

lettera_da_saltare = input("Inserisci una lettera:")
lettera_da_saltare = lettera_da_saltare.lower()

for i in parola:
    if i == lettera_da_saltare:
        continue
    print(i)
