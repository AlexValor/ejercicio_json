#Ejercicio libre.

#5. Pedir un rol y que te muestre los campeones que solamente sean rol único con el introducido, no pueden tener varios.


import json
from pprint import pprint

with open('campeoneslol.json') as data_file:
	data= json.load(data_file)

rolintroducido=input("Dime un rol: ")
contador=0
for nombre in data:
	for rol in nombre["tags"]:
		if rol == rolintroducido and len(nombre["tags"]) == 1:
			print(nombre["name"], "solamente es",rolintroducido, "no es un campeón híbrido")
			contador=contador+1
if contador == 0:
	print("No hay ningún campeón con",rolintroducido, "únicamente")	
		