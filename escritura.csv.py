import csv

encabezado = ["Nombre", "Película", "Comida"] 
cajero1 = ["Sara", "Drácula", "Crispetas"]
cajero2 = ["Juan", "Shrek", "Perro y nachos"]
cajero3 = ["Luisa", "El cadaver de la novia", "gaseosa"]

import csv

with open('salida.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow([encabezado])  
    escritor.writerow([cajero1])
    escritor.writerow([cajero2])
    escritor.writerow([cajero3])
    