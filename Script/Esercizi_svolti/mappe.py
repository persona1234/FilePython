""" Avete mai visto la barra di ricerca di google maps?
Qualsiasi luogo ricerchiamo viene inserito nel url e processato, c'è un modo per automatizzare una ricerca? Si.
"""

import webbrowser # Importo una libreria in grado di aprire pagine web

Luogo=input("Inserisci un luogo:") # Chiedo un luogo da inserire
webbrowser.open_new("https://www.google.com/maps/place/"+Luogo) # Aggiungo il luogo alla mia ricerca.

