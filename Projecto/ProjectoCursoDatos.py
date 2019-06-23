import requests
import pandas as pd
import numpy as np
import json
import num2words


#Funcion llamada del API


ced = input("Digite la cédula del empleado: ")
print(ced)

#ced= 110870778
datos = {'cedula': ced}

r = requests.get('http://127.0.0.1:5000/api/v1/resources/emp', params=datos)


#r = requests.get('http://127.0.0.1:5000/user/110870778')

print(r.status_code)

info_emp = r.json()
print(info_emp)

dict_emp = {}
dict_emp = info_emp


print('diccionario',dict)


template = "Constancia_salarial_template.docx"


#Funcion para insertar info en Doc de word

#SalarioNetoLetras = num2words(SalarioNeto,lang=es)



#Un dataframe no es tan efectivo como un dictionario para obtener los valores y pasarlos al word

#Convert a JSON string to pandas object with read_json

#esto si
#df3 = pd.DataFrame(pd.read_json(info_emp, typ='series').to_frame())

#print(df3.head())





