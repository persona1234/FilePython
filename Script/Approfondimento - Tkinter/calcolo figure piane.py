import math # Importo il modulo math contenente tutte le funzioni matematiche di cui avremo bisogno

print() # Stampo una riga vuota
print('<----------------------------------------------------------->') # Stampo una riga di decorazione
print("Hai bisogno di aiuto per calcolare l'area delle figure piane?") # Titolo del programma
print('<----------------------------------------------------------->') #  Stampo una riga di decorazione
print() # Stampo una riga vuota

while True:

    risposta=input(" Iniziare? si/no:" ) # Chiedo un input e lo inserisco in risposta.

    if risposta.lower()=='si': # Se la risposta trasformata in minuscolo è ugale a "si"

        figure=['Quadrato','Rettangolo','Cerchio','Trapezio','Triangolo','Rombo'] # Lista delle figure piane
        while True: # Fino a quando non viene inserito un numero ripeti quanto segue
            try:
                scelta=int(input('Digita 0 per Quadrato,\n 1 per Rettangolo,\n 2 per Cerchio,\n 3 per Trapezio,\n 4 per Triangolo,\n 5 per Rombo: ')) # digita un numero a seconda della tua figura
                break # concludi il ciclo
            except:
                print("Devi inserire un numero!") # informa l'utente che deve inserire un numero

        if scelta==0: # Ricorda che il primo elemento di una lista ha indice 0.
            print("Hai scelto di calcolare il quadrato!")
            l=int(input('Inserisci il valore del lato del quadrato:'))
            A=l**2 # Formula area
            print('La superficie misura..',A)
        elif scelta==1:
            print("Hai scelto di calcolare il rettangolo!")
            b=int(input('Dammi la base del rettangolo:'))
            h=int(input("Dammi l'altezza del rettangolo:"))
            A=b*h # Formula area
            print("L'area misura",A)
        elif scelta==2:
            print("Hai scelto di calcolare il cerchio!")
            raggio=int(input('Inserisci la misura del raggio:'))
            r=float(raggio)
            A=math.pi*r**2 # Formula area
            print("L'area misura: ",A)
        elif scelta==3:
             print("Hai scelto di calcolare il trapezio!")
             b=int(input('Dammi la base minore  del trapezio:'))
             B=int(input('Dammi la base maggiore del trapezio:'))
             h=int(input("Dammi l'altezza del trapezio:"))
             A=(b+B)*h/2 # Formula area
             print("L'area è:",A)
        elif scelta==4:
            print("Hai scelto di calcolare il triangolo!")
            b=int(input("inserisci la base del triangolo:"))
            h=int(input("inserisci l'altezza del triangolo:"))
            A=(b*h)/2 # Formula area
            print("L'area è uguale a",A)
        elif scelta==5:
            print("Hai scelto di calcolare il rombo!")
            D=int(input('Diagonale maggiore del rombo:'))
            d=int(input('Diagonale minore del rombo:'))
            A=d*D/2 # Formula area
            print("L'area è: ")
        else: print("AMICO, mi devi dare un numero da 0 a 5")
    else:
        print("ciao")
        break # Termina ciclo

                                
                            
    
