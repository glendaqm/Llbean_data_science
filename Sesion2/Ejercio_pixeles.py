pixel = [0.6, 0.3, 0.4]

a = pixel[0] + pixel[1] + pixel[2]

a = a/len(pixel)

listado = [8.999, 7.3, 10.4]

promedio = 0

promedio = sum(listado)/len(listado)

print(a)

print('promedio', promedio, 'redondeado', round(promedio))

#otra solucion con un loop

p = 0
for numero in pixel:
    p += numero

p = p / len(pixel)

print(p)


#hacer una logica para decidir si el pixel es blanco o negro. Blanco si es mayor a 0.5 sino es negro

if p > 0.5:
    print('es blanco')
else:
    print('es negro')

