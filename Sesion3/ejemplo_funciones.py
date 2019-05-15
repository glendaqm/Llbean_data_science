# crear una funcion que sume los numeros que se me den sin saber de antemano cuantos son


#definir la funcion
def sumar(*n):
    pass


#llamar a la funcion, aqui es donde se define que argumentos se le van a enviar
resultado = sumar(5,7,8,9,1)

#el doble asterisco dice que es un diccionario lo que va a recibir
def crear_dict(**n):
    pass

resultado = crear_dict(nombre='felix', apellido='arias', numero=10)

#en esta recibe dos argumentos diferentes, uno que puede ser cualquier cosa y el otro es un diccionario
def crear_lista_dict(*i,**n): #se usa (*args, kargs)
    pass

resultado = crear_lista_dict(4,5,'hola',nombre='felix', apellido='arias', numero=10)