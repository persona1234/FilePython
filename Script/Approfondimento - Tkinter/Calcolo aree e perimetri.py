from tkinter import * # Importo tutto da tkinter
from tkinter import messagebox # Importo da tkinter messagevoùùbox
import turtle # importo turtle
import math # importo math

#Creo una funzione di avvio
def avvio():
    # Controllare alla fine del programma, è lì che ho definito i vari widget che utilizzeremo.
    ciao="BENVENUTO,FAI UNA SCELTA:" # Variabile con il nome ciao
    testo.insert(END,ciao) # assegno alla casella di testo la variabile ciao, END non è importante per ora.
    AVVIO.destroy() # Distruggo AVVIO
    text.insert(END,"AREA:") # Inserisco nel widget text sempre il valore AREA
    per.insert(END,"PERIMETRO:")# inserisco nel widget per il testo PERIMETRO

    Bottone = Button(finestra, text="POL.REG", command=poligono_regolare) # Creo un pulsante dove finestra indica la finestra dove deve essere creato, text il testo assegnatogli e command la funzione da chiamare in caso di un click
    Bottone.pack(side="left", padx=50, pady=20)# posiziono il pulsante

    CERCHIO = Button(finestra, text="CERCHIO", command=circonferenza)
    CERCHIO.pack(side="left", padx=40, pady=50)

    RETTANGOLO = Button(finestra, text="RETTANGOLO", command=rettangolo)
    RETTANGOLO.pack(side="left", padx=30, pady=30)

    TRAPEZIO = Button(finestra, text="TRAPEZIO", command=trapezio)
    TRAPEZIO.pack(side="left", padx=30, pady=70)

#Funzione di uscita dal programma
def uscita():
    exita=messagebox.askokcancel(title="Messaggio di uscita", message="Vuoi davvero uscire?") # Creo un messagio di uscita
    if exita:
        exit()
#per i poligoni regolari
def poligono_regolare():

    # inizializzo turtle
    artista = turtle.Turtle() # Inizializzo la nostra tartaruga
    artista.color("red")
    #tento di ricevere dei dati ed elaborarli per formare una figura
    try:
        N =int(turtle.numinput("Domanda","Inserisci il numero dei lati di un poligono (compreso tra 3 e 12, 11 escluso):"))
        L=int(turtle.numinput("Domanda","Inserisci la misura del lato:"))

    except ValueError:
        print("Ehi! Devi inserire un numero intero...")
        N =int(turtle.numinput("Domanda","Inserisci il numero dei lati di un poligono (compreso tra 3 e 12, 11 escluso):"))
        L=int(turtle.numinput("Domanda","Inserisci la misura del lato:"))
    numero={3:0.289,4:0.5,5:0.688,6:0.866,7:1.038,8:1.207,9:1.374,10:1.539,12:1.866} # Creo un dizionario dove inserisco i numeri fissi
    numero_fisso = numero[N]
    apotema=(numero_fisso*L)
    perimetro=(N*L)
    area=(perimetro*apotema/2)

    text.insert(END,area)
    per.insert(END,perimetro)
    for i in range(N):
        artista.fd(L)
        artista.lt(360/N)
#per le circonferenze
def circonferenza():
    # inizializzo turtle
    artista = turtle.Turtle()
    artista.color("red")
    try:
        r = int(turtle.numinput("Raggio","Inserisci il raggio del cerchio:"))
        g = int(turtle.numinput("Gradi","Inserisci i gradi del cerchio:"))
    except ValueError:
        print("Ehi! Devi inserire un numero intero...")
        r = int(turtle.numinput("Raggio","Inserisci il raggio del cerchio:"))
        g = int(turtle.numinput("Gradi","Inserisci i gradi del cerchio:"))

    artista.circle(r,g)
    area=r**2*math.pi
    circon=(math.pi*2)*r
    #inserisco i valori nelle textbox
    text.insert(END,area)
    per.insert(END,circon)
    turtle.mainloop()

#per il rettangolo
def rettangolo():
    artista = turtle.Turtle()
    artista.color("red")
    try:
        base=int(turtle.numinput("Base","Inserisci la misura della base:"))
        altezza=int(turtle.numinput("Altezza","Inserisci la misura dell'altezza"))
    except ValueError:
        print("Ehi! Devi inserire un numero ")
        base=int(turtle.numinput("Base","Inserisci la misura della base:"))
        altezza=int(turtle.numinput("Altezza","Inserisci la misura dell'altezza"))

    area=base*altezza
    perim=(2*base+2*altezza)

    text.insert(END,area)
    per.insert(END,perim)
    for i in range(2):
        artista.fd(base)
        artista.lt(90)
        artista.fd(altezza)
        artista.lt(90)
    turtle.mainloop()

def trapezio():
    per.destroy()
    try:
        base_minore=int(turtle.numinput("Base","Inserisci la misura della base minore:"))
        base_maggiore=int(turtle.numinput("Base_Maggiore","Inserisci la  misura della base maggiore:"))
        altezza=int(turtle.numinput("Altezza","Inserisci la misura dell'altezza:"))
    except ValueError:
        print("Ehi! Devi inserire un numero ")
        base_minore=int(turtle.numinput("Base","Inserisci la misura della base minore:"))
        base_maggiore=int(turtle.numinput("Base_Maggiore","Inserisci la  misura della base maggiore:"))
        altezza=int(turtle.numinput("Altezza","Inserisci la misura dell'altezza:"))

    area=((base_minore+base_maggiore)*altezza)/2
    text.insert(END,area)

# Creo la finestra
finestra = Tk()
finestra.geometry("800x400+400+300")
finestra.title("CALCOLO AREE E PERIMETRI")
#caselle di testo
testo=Entry(finestra,width=53)
testo.pack()

text=Entry(finestra,width=40)
text.pack()

per=Entry(finestra,width=40)
per.pack()

#pulsanti
AVVIO = Button(finestra,text="AVVIO",command=avvio)
AVVIO.pack(side="left",padx=50,pady=20)
AVVIO.pack()

Esci=Button(finestra,text="ESCI",command=uscita)
Esci.pack(side="left",padx=30,pady=50)
Esci.pack()
Esci.pack()


#creo un menu
barra_menu=Menu(finestra)
menu_file = Menu(barra_menu, tearoff = 0)
menu_file.add_command(label="Esci", command=uscita)
menu_file.add_command(label="POL.REG",command=poligono_regolare)
menu_file.add_command(label="Cerchio", command=circonferenza)
menu_file.add_command(label="Rettangolo", command=rettangolo)
menu_file.add_command(label="Trapezio", command=trapezio)

barra_menu.add_cascade(label="Opzioni",menu=menu_file)
finestra.config(menu=barra_menu)
finestra.mainloop()
