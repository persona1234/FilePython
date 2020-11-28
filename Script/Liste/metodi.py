Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lista = [0,"Uno",2,"tre",4.0]
>>> lista.append("cinque")
>>> print(lista)
[0, 'Uno', 2, 'tre', 4.0, 'cinque']
>>> 
KeyboardInterrupt
lista2 = ["sei"]
>>> lista2 = ["sei"]
>>> lista.extend(lista2)
>>> print(lista)
[0, 'Uno', 2, 'tre', 4.0, 'cinque', 'sei']
>>> lista.sort()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    lista.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> #Non è possibile stabilire un ordine tra interi e stringhe
>>> alfabeto = ["a","d","b","k","l","z"]
>>> alfabeto.sort()
>>> print(alfabeto)
['a', 'b', 'd', 'k', 'l', 'z']
>>> numero = [1,5,2,3]
>>>  numero.sort()
 
SyntaxError: unexpected indent
>>> numero.sort()
>>> # Prima avevo messo uno spazio che non doveva esserci :(
>>> print(numero)
[1, 2, 3, 5]
>>> sum(numero)
11
>>> lista.pop()
'sei'
>>> #Ha tolto l'ultimo elemento
>>> lista.pop(1)
'Uno'
>>> #Ha tolto l'elemento nella seconda posizione, quindi con indice 1 e l'ha stampato
>>> lista.romove("tre")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    lista.romove("tre")
AttributeError: 'list' object has no attribute 'romove'
>>> #Remove no romove
>>> lista.remove("tre")
>>> #Ha rimosso l'elemento "tre" dalla lista e non ha stampato nulla
>>> s = "ciao come va?"
>>> l = s.split() #se lasciato senza delimitatore split divide ad ogni spazio
>>> print(l)
['ciao', 'come', 'va?']
>>> l = s.split("c") # Se invece dividessimo ad ogni c la lista generata sarà cosi:
>>> print(l)
['', 'iao ', 'ome va?']
>>> # ora facciamo il contrario
>>> st = "c".join(l)
>>> print (st)
ciao come va?
>>> # abbiamo impostato come delimitatore la c e ricreata la stringa
>>> 