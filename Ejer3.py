#Buscar o filtrar información. Pedir por teclado uno o varios datos y utilizarlos para hacer una búsqueda.

#3. Pedir por teclado cantidad de vida (hp) base y mostrar que campeones tienen mas de la indicada y su vida por nivel.

import json
from pprint import pprint

with open('campeoneslol.json') as data_file:
	data= json.load(data_file)

vida=int(input("Dime una cantidad de vida (hp): "))

for nombre in data:
	if nombre["stats"]["hp"] > vida:
		print(nombre["name"], "tiene más puntos de vida de lo indicado.")
		print("Tiene un total de:",nombre["stats"]["hp"])
		print("Y aumenta", nombre["stats"]["hpperlevel"], "vida por nivel.")
		print()