# Esempi vari per ottenere le dimensioni monitor, posizione del mouse e generare
# una finestra 

import pyautogui

dim = pyautogui.size()
print(dim)
posizione = pyautogui.position()
print(posizione)
# Le 4 varianti di finestre:
pyautogui.password("Ciao_sono_password")
pyautogui.prompt("Ciao_sono_Prompt")
pyautogui.alert("Ciao sono alert")
pyautogui.confirm("Ciao sono conferma")

