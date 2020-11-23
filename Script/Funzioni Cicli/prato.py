# Ripetere inserimento parola fino a "prato"

while True:
    parola = input("Inserisci una parola:")
    if parola == "prato":
        print("Indovinato!")
        break
    else:
        print("Ritenta")
print("Gioco terminato")
