# Tarea 1
# Escribir un código en Python que imprima en pantalla lo siguiente:
# * 3.1415926 ** 3.141592 *** 3.14159 **** 3.1415 ***** 3.141 ****** 3.14
# usando el operador % para definir la cantidad de digitos decimales de PI y la cantidad de asteriscos.
# https://cs.nyu.edu/courses/spring12/CSCI-UA.0002-007/Basic%20Formatting%20in%20Python.pdf

pi = '3.1415926'
asteriscos = '******'


print(("%.1s %.9s") % ( asteriscos, pi ),("%.2s %.8s") % ( asteriscos, pi ), ("%.3s %.7s") % ( asteriscos, pi ), ("%.4s %.6s") % ( asteriscos, pi ), ("%.5s %.5s") % ( asteriscos, pi ), ("%.6s %.4s") % ( asteriscos, pi ))


#intentando hacerlo con un loop

#frase = ''

#for i in range(1, 5):
    #frase = frase + "%.[i]s %.[9-1]s" % ( asteriscos, pi )

#print(frase)


