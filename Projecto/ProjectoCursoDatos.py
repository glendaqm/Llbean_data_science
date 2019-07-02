# importamos la libreria para hacer mailmerge (adicion automatica de nombres y direcciones de una DB a cartas, sobres para facilitar el envio de correo especialmente masivo
from __future__ import print_function
from mailmerge import MailMerge

#libreria para construir y manejar HTTP requests
import requests
#esta libreria es para convertir una cifra en numeros a letras
import num2words
#import json



#Creamos una Funcion para llamar al web service

#pedir al usuario que digite la cedula del empleado para generar la constancia
ced = input("Digite la cédula del empleado: ")
print(ced)

# Creamos un HttP request (get) para invocar al web service y pasar la cedula digitada como parametro del request
# Recordemos que el web service esta esperando el metodo get
datos = {'cedula': ced}
r = requests.get('http://127.0.0.1:5000/api/v1/resources/emp', params=datos)

#imprimir el status code del response, si fue exitoso imprime un 200
print(r.status_code)

#se crea un diccionario con el json que viene del response para la cedula consultada
dict_emp = {}

#esto lo que va a hacer es quitar el primer elemento del diccionario para que solo quede la info que viene del web service
dict_emp = r.json()[-1]

# imprimimos el contenido para ver que informacion nos trajo
print(dict_emp)

# guardamos el template de la constancia en la variable template
template = "Constancia_salarial_template.docx"

#Creamos un documento mailmerge que contiene la informacion del template
document = MailMerge(template)
#imprimimos el contenido del objeto para ver todos los campos a llenar que contiene
print(document.get_merge_fields())


#Funcion para insertar info en Doc de word




#Funcion para calcular el salario Neto, recibe el salario bruto por parametro
#calculo de renta:
#817 - 1,226: 10%
#1,226 - 2,103: 15%
#2,103 - 4,205: 20%
#4,205+ : 25%

def calcSalarioNeto(salarioBruto) :
    salarioNeto = 0
    caja = salarioBruto * 0.1034
    renta = 0
    if (salarioBruto <= 817000) :
        renta = renta
    else :
        renta = (1226000 - 817000) * 0.10
        if (salarioBruto > 1226000):
            if (salarioBruto <= 2103000):
                renta = renta + ((salarioBruto - 1226000) * 0.15)
            else: # mayor a 2,103,000
                renta = renta + ((2103000 - 1226000) * 0.15)
                if (salarioBruto <= 4205000):
                    renta = renta + ((salarioBruto - 2103000) * 0.20)
                else : # mayor a 4,205,000
                    renta = renta + ((4205000 - 2103000) * 0.20)
                    renta = renta + ((salarioBruto - 4205000)* 0.25)

    salarioNeto = salarioBruto - caja - renta
    return salarioNeto



# Llamamos a la funcion que calcula el salario Neto y guardamos el valor que devuelve en el diccionario
dict_emp['salarioNeto']=calcSalarioNeto(dict_emp['salarioBruto'])

# Guardamos la version en letras del salario Neto y Bruto
netoLetras = num2words.num2words(dict_emp['salarioNeto'],lang='es')
brutoLetras = num2words.num2words(dict_emp['salarioBruto'],lang='es')


#print(' salario neto', netoLetras)
#print(' salario bruto', brutoLetras)

#con la funcion merge vamos a asignarle un valor a cada campo que hay que rellenar en la constancia
document.merge(

    Cedula=str(dict_emp['cedula']),
    Departamento=dict_emp['departamento'],
    SalarioBruto=str(dict_emp['salarioBruto']),
    Puesto=dict_emp['puesto'],
    NombreEmpleado=dict_emp['nombre']+' '+dict_emp['apellido1']+' '+dict_emp['apellido2'],
    FechaIngreso=dict_emp['fecha_ingreso'],
    SalarioNeto= str(dict_emp['salarioNeto']),
    SalarioNetoLetras=str(netoLetras) + ' colones',
    SalarioBrutoLetras=str(brutoLetras)+' colones'
)

#creamos un archivo usando el template y la informacion del empleado que insertamos
document.write('test-output.docx')


