import turtle # Importo turtle
bob=turtle.Turtle()
""" Assegno a turtle il nome del "pittore",
in questo caso Bob, capirete presto perché
"""
def quadrato(bob,lunghezza): #Definisco una funzione con argomenti bob e lunghezza
    for i in range(4): # Ripeti per 4 volte quanto segue:
        bob.fd(lunghezza) #Vai dritto per quanto misura lunghezza
        bob.lt(90) # Gira a sinistra di 90 gradi
quadrato(bob,100) # Chiamo la funzione con argomenti bob e il valore della lunghezza
turtle.mainloop() # Avvio il tutto

#L'avete capito? Disegna un quadrato
