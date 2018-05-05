#Listar información. Ejercicio que liste cierta información.

#1.Lista los nombres de los campeones y sus roles.

import json
from pprint import pprint

with open('campeoneslol.json') as data_file:
	data= json.load(data_file)


for nombre in data:
	print(nombre["name"])
	print("-------")
	for rol in nombre["tags"]:
		print(rol)
	print()