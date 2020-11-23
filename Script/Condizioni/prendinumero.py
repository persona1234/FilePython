"""
In questo script stiamo controllando se il numero 
inserito dall'utente è positivo, negativo o è zero
"""
numero = int(input("Inserisci un numero:"))
"""chiedo un numero all'utente che viene convertito in intero.
E' possibile controllare il risultato di tale conversione con il comando print(type())
"""

if numero >0:
    print("Il numero è positivo")
elif numero == 0:
    print("Il numero è zero")
    """utilizzo il doppio uguale per controllare se il numero è uguale a 0,
se ne avessi usato solo uno avrei assegnato al numero il valore di 0,
come nel caso dell'assegnazione alla variabile "numero"
"""
else:
    print("Il numero è negativo")


