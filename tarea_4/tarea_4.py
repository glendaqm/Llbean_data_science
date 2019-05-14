#Tarea_4


hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]

print(hoja_calculo)

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

b = transpuesta(hoja_calculo)
b #sea b la tabla resultante luego de aplicar transpuesta

#Parte 3 - actualizar los creditos con 20%, si lo corro aqui si funciona pero al final no
#b[2] = list(map(lambda x: x*1.20, b[2]))
#print('Creditos actualizados:', b)

#Parte 1
#Contruya un diccionario de funciones matematicas (utilizando funciones lambda) entre todos los números de la lista tales como:


#Promedio

prom_saldos = lambda x : sum(x)/len(x)
a= prom_saldos(b[1])
print('esto es promedio:',a)


#La Multiplicacion
'''
def multi_cred(cred):
    result = 1
    for i in cred:
        result = result * i
    return result

c = multi_cred(b[2])
print('esto es mult:',c)
'''

multi = lambda x,y,z : x*y*z
c = multi(b[1][0], b[1][1], b[1][2])
print('esto es mult:',c)

#La suma

sum_deudas = lambda x : sum(x)
b  = sum_deudas(b[3])
print('esto es suma:', b)



#dict_funciones = {'promedio':lambda: sum(b[1])/len(b[1])}


dict_funciones = {'promedio':a, 'suma':b, 'multiplicacion':c}

print(dict_funciones)



#Parte 2
#Obtenga utilizando el diccionario de funciones:

#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en promedio todas las personas.

print('¿Cuánto tienen en promedio todas las personas?:',dict_funciones['promedio'])

#2. La suma de todas las deudas

print('Suma de todas las deudas:',dict_funciones['suma'])

#3. la multiplicación de todos los crédito entre si

print('Multiplicacion de creditos:',dict_funciones['multiplicacion'])


#Parte 3
#Actualice (en la tabla general)los valores de los créditos aplicando un impuesto del 20% (esto es multiplicar por 1.2) a toda la fila de créditos usando el diccionario de funciones.

print('este codigo me da error: TypeError: float object is not subscriptable pero si lo corro antes si funciona')

'''b[2] = list(map(lambda x: x*1.20, b[2]))
print('Creditos actualizados:', b)'''