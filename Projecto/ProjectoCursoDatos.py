import requests
import pandas as pd
import numpy as np
import json
import num2words


#Funcion llamada del API


params = '110870778'

r = requests.get('http://127.0.0.1:5000/user/110870778')

print(r.status_code)

info_emp = r.json()
print(info_emp)
print(len(info_emp))


#Un dataframe no es tan efectivo como un dictionario para obtener los valores y pasarlos al word

#Convert a JSON string to pandas object with read_json

df3 = pd.DataFrame(pd.read_json(info_emp, typ='series').to_frame())

print(df3.head())


#df = pd.DataFrame(records)


#dataframe = pd.DataFrame(columns=r.json()[0].keys())


#Funcion para insertar info en Doc de word

#
#SalarioNetoLetras = num2words(SalarioNeto,lang=es)



#json_normalize(r)


