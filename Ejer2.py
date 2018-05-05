#Contar información. Ejercicio que muestre el total de veces que aparece una información

#2. Muestra el total de campeones que tienen un rango mayor que 500.

import json
from pprint import pprint

with open('campeoneslol.json') as data_file:
	data= json.load(data_file)

contador=0

for nombre in data:
	if nombre["stats"]["attackrange"] > 500:
		contador=contador+1
print("Hay un total de",contador,"campeones con más rango que 500")