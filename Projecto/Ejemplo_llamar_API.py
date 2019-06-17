import requests
import pandas as pd
import numpy as np
import json
#from token import token


#import json
#from token import token
#from pandas.io.json import json_normalize

#hacer un request y guardarlo en objeto r que es el response
#r = requests.get('https://api.github.com/events')
#verificar el status code del request, 200 es bueno
#r.status_code
#obtener la repuesta en forma de json
#r.json()


params = {'country': 'AR'}

r = requests.get('https://api.openaq.org/v1/cities', params)


print(r.status_code)

records = r.json()['results']
print(records)
print(len(records))

df = pd.DataFrame(records)

pass

dataframe = pd.DataFrame(columns=r.json()['results'][0].keys())


print(df.head())

print(dataframe.head())


#json_normalize(r)

