# crear un archivo csv con una lista de contectos telefono
'''
nombre,apellido,telefono
paco,alfaro,78943
carlos,mora,747320
'''


import csv

misDatos = [["nombre", "apellido", "telefono"],
          ['Paco', 'Alfaro', '78943'],
          ['Carlos', 'Mora', '747320']]

miArchivo = open('contactos_telefono.csv', 'w')
with miArchivo:
    writer = csv.writer(miArchivo)
    writer.writerows(misDatos)

print("Archivo csv creado")


'''
import csv
 
lista = [1,2,3]
 
file = open("eggs.csv", "w", newline='')
spamreader = csv.writer(file)
spamreader.writerow(lista)
file.close()
'''