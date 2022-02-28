import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

with open('/Users/LORENA MASTER/Desktop/BuenasPracticas/leccion1/finanzas2020[1].csv', newline='') as csvfile:
	read_csv = csv.reader(csvfile, delimiter='\t')
	dataset = []
	for row in read_csv:
		dataset.append(row)

processed_data = []
for i in range(1, len(dataset)):
	aux_dataset = []
	for j in dataset[i]:
		try:
			aux = int(j)
			aux_dataset.append(aux)
		except:
			aux_dataset.append(0)
			print("No puedo convertir el valor ", j)
	processed_data.append(aux_dataset)

print(processed_data)


df=pd.DataFrame(processed_data)

print(df)

maxValor=df[[0,1,2, 3,4,5,6,7,8,9,10,11]].max()
print("Máximos valores en columnas: ")
print(maxValor)



minValor=df[[0,1,2, 3,4,5,6,7,8,9,10,11]].min()
print("Minimos valores en columnas: ")
print(minValor)


medValor=df[[0,1,2, 3,4,5,6,7,8,9,10,11]].mean()
print("\nMedia de los valores en columnas: ")
print(medValor)




#Errores

try:
	fichero = open ('/Users/LORENA MASTER/Desktop/BuenasPracticas/leccion1/finanzas2020[1].csv', "r")
	lines = fichero.readlines()
	print(lines)

except IOError:
	print("No encuentro el fichero.Error", err)

else:
	print("He leido el fichero sin problema. Lo cierro y termino.")
	fichero.close()
