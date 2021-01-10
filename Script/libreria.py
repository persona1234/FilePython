"""
Scrivi uno script in grado di chiedere all'utente un testo, se il libro è presente venderlo diminuendo il numero di copie disponibili, altrimenti ordinandolo e dirlo all'utente
"""

# L'idea mi è sorta cercando in rete e trovando un esercizio abbastanza simile

"""                
 #                                                                                 
 #            #      #####       #####       ######      #####       #        ##   
 #            #      #    #      #    #      #           #    #      #       #  #  
 #            #      #####       #    #      #####       #    #      #      #    # 
 #            #      #    #      #####       #           #####       #      ###### 
 #            #      #    #      #   #       #           #   #       #      #    # 
 #######      #      #####       #    #      ######      #    #      #      #    #                                                                                 
"""

#Creo un dizionario a cui associo ad ogni titolo il numero di copie presenti
libri_presenti = {"Harry Potter e la pietra filosofale":10,"Il piccolo principe":8,"Il signore degli anelli":5,"A Christmas Carol":2}

#Lista degli ordini
libri_mancanti = []


while True:
    # Richiesta di continuo/inizio
    richiesta = input("Vuoi continuare?(s/n)")
    # Se la richiesta in minuscolo è una n
    if richiesta.lower()=="n":
        exit()
    # Altrimenti
    else:
        libro_richiesto = input("Inserisci il titolo di un libro:")

        if libro_richiesto in libri_presenti:
            print(f"Il libro {libro_richiesto} è stato trovato.")
            # Diminuisco il numero di copie di uno
            libri_presenti[libro_richiesto] -=1

            if libri_presenti[libro_richiesto] == 0:
                libri_presenti.pop(libro_richiesto)

        else:
            print(f"Il libro {libro_richiesto} non è presente, ordine in corso...")
            print(f"Ecco i libri presenti: {libri_presenti}")
            libri_mancanti.append(libro_richiesto)


