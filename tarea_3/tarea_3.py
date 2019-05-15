#Tarea 3

# Para definir la agenda del hospital
agenda_hospital = []
persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')

# agregamos una persona
agenda_hospital.append(persona)

# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)


# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')

# agregamos otra persona
agenda_hospital.append(persona)

# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)

# suponga que vienen 5 personas mas
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]

# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)

print(agenda_hospital)

# notemos que la impresión en pantalla está un poco sucia... lo arreglamos
for paciente in agenda_hospital:
    print(paciente)


#Primera pregunta
#Cuantos pacientes llegaron en total?
print('Pacientes en total:',len(agenda_hospital))

#Segunda pregunta
#Cuantas personas llegaron por dolor?

cont = 0
for lista in agenda_hospital:
    contador = lista.count('dolor')
    cont = cont + contador

print('Pacientes con dolor:',cont)

#Tercera pregunta
#Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor. Ordene la lista desde el más adulto al más joven


agenda_hospital.sort(key=lambda x: x[3],reverse=True)

print('lista en orden de edad mayores primero', agenda_hospital)

#Cuarta Pregunta
#Cuantos pacientes son mayores de edad? cuantos menores?


mayores = 0
menores = 0
for lista in agenda_hospital:
    edad = lista[3]
    if edad > 18 :
        mayores = mayores + 1
    else:
        menores = menores + 1

print('Pacientes mayores:',mayores)
print('Pacientes menores:',menores)


#Quinta Pregunta
#Suponga que se atienden con orden de prioridad por gravedad de consulta, empezando por los que tienen dolor y
# luego por edad (mas viejo al joven), empezando por el adulto mayor. Ordene la lista empenzando por los
# que tienen mayor prioridad.

agenda_dolor = []
agenda_sin_dolor = []
agenda_hospital4 = []
agenda2 = []
agenda3= []

for lista in agenda_hospital:
    if 'dolor' in lista:
        agenda_dolor.append(lista)
    else:
        agenda_sin_dolor.append(lista)

sorted(agenda_dolor,key=lambda x: x[3],reverse=True)
print('lista solo dolor ordenada', agenda_dolor)
sorted(agenda_sin_dolor,key=lambda x: x[3], reverse=True)

print('lista sin dolor ordenada', agenda_sin_dolor)

agenda_hospital4.extend(agenda_dolor)
print('lista con primeros valores ordenados', agenda_hospital4)
agenda_hospital4.extend(agenda_sin_dolor)
print('Lista completa ordenado padecimiento y edad:',agenda_hospital4)

#Sexta pregunta
#Suponga que los que tienen dolor mueren :( Como queda la lista de pacientes vivos por atender
# ordenados por orden de edad desde el joven al viejo.


for i in agenda_hospital:
    lista = list(i)
    if 'dolor' in lista:
        agenda_hospital.remove(i)
    pass
print('lista sin dolor!',agenda_hospital)



#Segunda parte

'''
Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
Funcionamiento sugerido

Dígame cuántas palabras tiene la lista: 3
Dígame la palabra 1: Alberto
Dígame la palabra 2: Benito
Dígame la palabra 3: Carmen
La lista creada es: ['Alberto', 'Benito', 'Carmen']
Dígame cuántas palabras tiene la lista: 0
¡Imposible!
'''


