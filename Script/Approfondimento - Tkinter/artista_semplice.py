# Disegnarore di poligoni
  
import turtle

artista = turtle.Turtle() 

lati = int(input("Numero dei lati: ")) 
lunghezza = int(input("Lunghezza lati: ")) 
  
  
for i in range(lati): 
    artista.forward(lunghezza) 
    artista.right(360/lati) 
