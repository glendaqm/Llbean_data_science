#Tarea 2

#Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.
#Ejemplo mis_valores = [5, 6, 10, 13, 3, 4]

mis_valores = [5, 6, 10, 13, 3, 4]

promedio = sum(mis_valores)/len(mis_valores)

print('Ejercicio 1 \n''Promedio: ',"%.2f" % (promedio),'\n')

# Considere si se tiene una lista que contiene las alturas de grupos de personas

todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]

#Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas

altura = 0
mayor_altura= 0
numero_grupo= 0
grupo = ''
for i in todos:
    altura= max(i)
    numero_grupo = numero_grupo + 1
    if altura > mayor_altura:
        mayor_altura = altura
        grupo = 'Grupo ' + str(numero_grupo)

print('Ejercio 2\nGrupo con mayor altura: ',grupo)
print('Mayor altura: ',mayor_altura)