from __future__ import print_function
from mailmerge import MailMerge
#from datetime import date


import requests
import num2words
#import json



#Funcion llamada del API

#pedir al usuario la cedula del empleado para generar la constancia
ced = input("Digite la cédula del empleado: ")
print(ced)

#Llamar al web service y pasar la cedula digitada por parametro
datos = {'cedula': ced}
r = requests.get('http://127.0.0.1:5000/api/v1/resources/emp', params=datos)

#imprimir el status code del response
print(r.status_code)

#se crea un diccionario con el json que viene del response para la cedula consultada
dict_emp = {}
#esto lo que va a hacer es quitar el primer
dict_emp = r.json()[-1]
print(dict_emp)


template = "Constancia_salarial_template.docx"

#To create a mailmerge document and look at all of the fields:
document = MailMerge(template)
print(document.get_merge_fields())




#Funcion para insertar info en Doc de word

#SalarioNetoLetras = num2words(SalarioNeto,lang=es)

#817 - 1,226: 10%
#1,226 - 2,103: 15%
#2,103 - 4,205: 20%
#4,205+ : 25%


'''
def calcSalarioNeto(salarioBruto) :
    salarioNeto = 0
    renta = 0
    caja = salarioBruto = (salarioBruto * 10.34)
    if (salarioBruto <= 817,000) :
        renta = renta
    elif (salarioBruto > 817,000 and salarioBruto <= 1,226,000) :
        renta = renta + ((salarioBruto - 817,00) * 0.10)
    elif (salarioBruto > 1,226,000 and salarioBruto <= 2,103,000):
        renta = renta + ((salarioBruto - 1,226,000) * 0.15)
    elif (salarioBruto > 2,103,000 and salarioBruto <= 4,205,000):
        renta = renta + ((salarioBruto - 2,103,000) * 0.20)
    else :
        renta = renta + ((salarioBruto - 4,205,000)* 0.25)

    salarioNeto = salarioBruto - caja - renta
    return salarioNeto

'''

dict_emp['salarioNeto']= 50000
#dict_emp['salarioNeto']=calcSalarioNeto(dict_emp['salarioBruto'])

netoLetras = num2words.num2words(dict_emp['salarioNeto'],lang='es')
brutoLetras = num2words.num2words(dict_emp['salarioBruto'],lang='es')

print('bruto', brutoLetras)

print(document.get_merge_fields())


document.merge(

    Cedula=str(dict_emp['cedula']),
    Departamento=dict_emp['departamento'],
    SalarioBruto=str(dict_emp['salarioBruto']),
    Puesto=dict_emp['puesto'],
    NombreEmpleado=dict_emp['nombre']+' '+dict_emp['apellido1']+' '+dict_emp['apellido2'],
    FechaIngreso=dict_emp['fecha_ingreso'],
    #calcSalarioNeto(dict_emp['salarioBruto']),
    SalarioNeto= str(dict_emp['salarioNeto']),
    SalarioNetoLetras=str(netoLetras) + ' colones',
    SalarioBrutoLetras=str(brutoLetras)+' colones'
)


document.write('test-output.docx')


#Un dataframe no es tan efectivo como un dictionario para obtener los valores y pasarlos al word

#Convert a JSON string to pandas object with read_json

#esto si
#df3 = pd.DataFrame(pd.read_json(info_emp, typ='series').to_frame())

#print(df3.head())

