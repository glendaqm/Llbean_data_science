# Esto es un ejemplo de tuplas

#Crear una tupla de 5 elementos de tipos diferentes

tupla1 = (1,5,10.5,'Glenda', True)

print('Este es el contenido de mi Tupla:', tupla1)

#agregar mas elementos

tupla1 = tupla1 + ('otro', 5, False)

print(tupla1)

#acumular elementos

tupla1 += ('otro', 5, False)

print(tupla1)

#subtupla
#el segundo hasta el penultimo elemento. El valor -1 es el ultimo pero al estar al lado derecho es exclusive

print(tupla1[1:-1])

#imprimir del segundo al final
print(tupla1[1:])


#subtupla con saltos
#los elementos pares osea el indice cero, el indice 2, el indice 4
print('los elementos pares de la tupla: ', tupla1[::2])

#tira todos los elementos porque va de uno en uno
print('los elementos pares de la tupla: ', tupla1[::1])

#imprime los impares, porque empieza desde la posicion dos y luego salta de dos en dos
print('los elementos pares de la tupla: ', tupla1[1::2])

#imprime de tres en tres
print('los elementos pares de la tupla: ', tupla1[::3])






