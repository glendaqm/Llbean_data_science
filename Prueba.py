hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]

print(hoja_calculo)

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

b = transpuesta(hoja_calculo)
b #sea b la tabla resultante luego de aplicar transpuesta



def multi_cred(cred):
    result = 1
    for i in cred:
        result = result * i
    return result

valor = multi_cred(b[2])

print(valor)


#from functools import reduce
#c = reduce((lambda x, y: x * y), b[3])

#multi_cred = lambda x,y,z : x*y*z
#c = multi_cred(b[2[1]],b[2[2]],b[2[3]])
#result = 1
#multi_cred=lambda x : (for i in x: result = result * i)
#multi_cred = lambda x: list(map(x*x, x))
'''
def multi_cred(cred):
    result = 1
    for i in cred:
        result = result * i
    return result

'''
#print(b[2])

#multi_cred(b[2])

'''
def multi_cred(cred):
    result = 1
    for i in cred:
        result = result * i
    return result

ac= multi_cred(b[2])
'''

#print('esto es c:', ac)

#dict_funciones = { 'prom_saldos':23.20, 'suma_deudas':9.92, 'multip_creditos':475.96}







#promedio=sum(b[1])/ len(b[1])




'''
def prom(x):
    return sum(x)/len(x)
bb = prom(b[1])

print('lo hice:',bb)

prom = lambda x : sum(x)/len(x)
a= prom(b[1])

print('lo hice denuevo:',a)

'''
