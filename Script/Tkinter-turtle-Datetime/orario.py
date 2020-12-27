from datetime import datetime
orario_ora  = datetime.today()
print(orario_ora)
# E' possibile ottenere una determinata porzione della data in questo modo:

print("Anno:",orario_ora.year)
print("Mese:",orario_ora.month)
print("Giorno:",orario_ora.day)
print("Ora:",orario_ora.hour)
print("Minuti:",orario_ora.minute)
print("Secondi:",orario_ora.second)
