
'''

identificación
Nombre
Apellido
teléfono
dirección
lista de enfermedades tratadas
lista de medicamentos que toma

'''

class paciente:

    def __init__(self, ced, nombre, ape, tel, dir):
        self.ced = ced
        self.nombre = nombre
        self.ape = ape
        self.tel = tel
        self.dir = dir
        self.listaEnfermedades = []
        self.listaMedicamentos = []

    def add_enfermedad(self, enfermedad):
        self.listaEnfermedades.append(enfermedad)

    def add_medicamento(self, medicamento):
        self.listaMedicamentos.append(medicamento)





'''
Operaciones:

Ingreso de un paciente nuevo
Borrado de un paciente
Agregar más enfermedades en un paciente en particular
Agregar más medicamentos en un paciente en particular
Generar reporte de las enfermedades tratadas en la clínica
Generar reporte de los medicamentos entregados en la clínica
Comparar 2 pacientes en particular: cuales enfermedades tienen en común. Cuales no?. Lo mismo con los medicamentos.

Consideraciones:

La lista inicial de pacientes puede estar escrito en el código asi como su información. 
La implementación puede ser abierta: puede ser que cada paciente sea creado por una clase o 
simplemente cada paciente sea un diccionario con toda la información solicitada.
'''

def agregarPaciente (paciente, listaPacientes):
    listaPacientes.append (paciente)
    return listaPacientes


def borrarPaciente (paciente, listaPacientes):
    listaPacientes.remove(paciente)
    return listaPacientes

def repEnfTratadas(listaPacientes):
    enfermedades = []
    for i in listaPacientes:
        enfermedades.append(i.listaEnfermedades)
    return enfermedades


def repMedEntregados(listaPacientes):
    medicamentos = []
    for i in listaPacientes:
        medicamentos.append(i.listaMedicamentos)
    return medicamentos



Paciente1 = paciente(123,'Glenda', 'Quesada', '8855-8855', 'Alajuela')

Paciente1.add_enfermedad('Cansancio crónico')
Paciente1.add_enfermedad('Presión baja')
Paciente1.add_medicamento('Cafeina')
Paciente1.add_medicamento('Confites')

Paciente2 = paciente(456, 'Harry', 'Potter', '6677-6677', 'Little Whinging')

Paciente2.add_enfermedad('Diabetes')
Paciente2.add_enfermedad('Ammesia')
Paciente2.add_medicamento('Insulina')
Paciente2.add_medicamento('Camote')

Paciente3 = paciente(678,'Arya', 'Stark', '9900-9900', 'Unknown')

Paciente3.add_enfermedad('Insomnio')
Paciente3.add_enfermedad('Anemia')
Paciente3.add_medicamento('Melatonina')
Paciente3.add_medicamento('Pastillas de Hierro')

#Ingreso de un paciente nuevo
listaPacientes1 = []
listaPacientes1 = agregarPaciente(Paciente1,listaPacientes1)
listaPacientes1 = agregarPaciente(Paciente2, listaPacientes1)
listaPacientes1 = agregarPaciente(Paciente3, listaPacientes1)


#Borrado de un paciente
listaPacientes1 = borrarPaciente(Paciente1, listaPacientes1)


#Agregar más enfermedades en un paciente en particular
Paciente2.add_enfermedad('Insomnio')

Paciente2.add_medicamento('Melatonina')


#Generar reporte de las enfermedades tratadas en la clínica
print('Reporte Enfermedades Tratadas: ', repEnfTratadas(listaPacientes1))


#Generar reporte de los medicamentos entregados en la clínica
print('Reporte Medicamentos Entregados: ', repMedEntregados(listaPacientes1))


#Comparar 2 pacientes en particular: cuales enfermedades tienen en común.

def coincidencias(a, b):
    a = set(a)
    b = set(b)
    return list(b & a)

print('Enfermedades en común entre pacientes',Paciente2.nombre,'y',Paciente3.nombre,':',coincidencias(Paciente2.listaEnfermedades, Paciente3.listaEnfermedades))

print('Medicamentos en común entre pacientes',Paciente2.nombre,'y',Paciente3.nombre,':',coincidencias(Paciente2.listaMedicamentos, Paciente3.listaMedicamentos))


def diferentes(a, b):
    a = set(a)
    b = set(b)
    return [list(b - a), list(a - b)]

# Cuales no?. Lo mismo con los medicamentos.

print('Enfermedades distintas entre pacientes',Paciente2.nombre,'y',Paciente3.nombre,':',diferentes(Paciente2.listaEnfermedades, Paciente3.listaEnfermedades))

print('Medicamentos distintos entre pacientes',Paciente2.nombre,'y',Paciente3.nombre,':',diferentes(Paciente2.listaMedicamentos, Paciente3.listaMedicamentos))