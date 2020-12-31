import subprocess


data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
for i in data:
    if "Tutti i profili utente" in i:
        i=i.replace("Tutti i profili utente    :","")
        i=i.strip()
        risultati = subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode("utf-8", errors="backslashreplace").split("\n")
        for line in risultati:
            if "Contenuto chiave" in line:
                print(i,line)
    
