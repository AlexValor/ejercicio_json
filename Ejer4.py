#Buscar información relacionada.

#4.Pide por teclado el nombre de un campeón y te mostrará su título y su descripción.

import json
from pprint import pprint

with open('campeoneslol.json') as data_file:
	data= json.load(data_file)

campeon=input("Dime el nombre de un campeón: ")

for nombre in data:
	if nombre["name"] == campeon:
		print("Su título es:", nombre["title"])
		print("Descripción:")
		print(nombre["description"])