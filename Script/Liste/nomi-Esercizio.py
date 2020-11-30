nomi = []
while True:
    nome = input("Inserisci qualche nome:")
    nomi.append(nome)
    nomi.sort()
    if nome == "fine":
        print(nomi)
    else:
        pass
