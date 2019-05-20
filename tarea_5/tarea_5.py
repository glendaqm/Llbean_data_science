
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
    #pregunta: inicializar en [] es necesario?
    enfermedades = []
    for i in listaPacientes:
        pacienteTemp = paciente(i)
        enfermedades.append(pacienteTemp.listaEnfermedades)
    return enfermedades


def repMedEntregados(listaPacientes):
    for i in listaPacientes:
        pacienteTemp = paciente(i)
        medicamentos=medicamentos.append(pacienteTemp.listaMedicamentos)
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

listaPacientes1 = []
listaPacientes1 = agregarPaciente(Paciente1,listaPacientes1)
listaPacientes1 = agregarPaciente(Paciente2, listaPacientes1)
listaPacientes1 = agregarPaciente(Paciente3, listaPacientes1)

listaPacientes1 = borrarPaciente(Paciente1, listaPacientes1)


print('Reporte Enfermedades Tratadas: ', repEnfTratadas(listaPacientes1))

print('Reporte Medicamentos Entregados: ', repMedEntregados(listaPacientes1))

'''
listaPacientes = {
    "id":1234, "nombre": 'Glenda', "apellido":'Quesada',"tel":8311,"dir":'Alajuela',"enfermedades":'demencia y presion alta', "medicamentos":'naturales'
  }

'''