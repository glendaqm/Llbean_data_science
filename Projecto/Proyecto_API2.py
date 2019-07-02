#importamos una libreria o web framework para crear web applications y APIs. Hay otras como Django y CherryPy
import flask
from flask import request, jsonify

#Creamos el objeto applicación de tipo Flask para crear nuestro web application (o web service),
# que contiene información acerca de la aplicación y también métodos (funciones)
#que le dicen a la aplicación que haga ciertas cosas, como la función "run"

app = flask.Flask(__name__)
#Le decismos que nos deje hacer "debugging" para que podamos ver errores cuando ejecutemos el
# código de la aplicación
app.config["DEBUG"] = True


#Creamos una lista de Diccionarios con la información de los empleados que vamos a necesitar para la constancia.
# En la vida real Workday lo obtiene de una base de datos, no están los datos en caliente

empleados = [
    {
        "cedula": 110870778,
        "nombre": "Glenda",
        "apellido1": "Quesada",
        "apellido2": "Monge",
        "fecha_ingreso": "21 de Agosto del 2006",
        "puesto": "IS Manager III",
        "departamento":"Information Services",
        "salarioBruto":300000
    },
    {
        "cedula": 114380418,
        "nombre": "Cristina alias Titi",
        "apellido1": "Penon",
        "apellido2": "Portman",
        "fecha_ingreso":"2 de Enero del 2009",
        "puesto": "Analyst III",
        "departamento":"EIM Reporting",
        "salarioBruto":400000
    },
    {
        "cedula": 900010783,
        "nombre": "Julia",
        "apellido1": "Monge",
        "apellido2": "Quesada",
        "fecha_ingreso":"16 de Junio del 2019",
        "puesto": "Asistente Administrativa",
        "departamento":"Recursos Humanos",
        "salarioBruto":5000000
    },
    {
        "cedula": 110250162,
        "nombre": "Esteban",
        "apellido1": "Chavarria",
        "apellido2": "Vega",
        "fecha_ingreso":"13 de Mayo del 2019",
        "puesto": "Sourcing Manager",
        "departamento":"Global Procurement",
        "salarioBruto":500000
    }
]

#El proceso de mapear URLs a funciones se llama routing. La sintaxis @app.route('/', methods=['GET']) es la parte
# del programa que le deja saber a Flask que esta función "api_empleado" se debe asociar al path: /api/v1/resources/emp
# La lista methods (methods=['GET']) es un parametro de la funcion route que le permite a Flask saber qué tipo
#de HTTP requests son permitidos. En este caso nos interesa hacer un Get (el get y especificar un path son parte de
#las reglas del protocolo HTTP y no se python o de Flask)


@app.route('/api/v1/resources/emp', methods=['GET'])
def api_empleado():
    # Verifica si la cedula es parte del URL. Si la cédula es provista, la asigna a una variable para guardarla.
    # Si no, despliega un error en el browser.
    if 'cedula' in request.args:
        cedula = int(request.args['cedula'])
    else:
        return "Error: La cédula no fue provista. Por favor especifique una."

    # Creamos una lista vacía llamada resultados, donde vamos a guardar la info
    # del empleado si es encontrado por medio de la cédula
    results = []

    # Recorremos la lista empleados para ver si encontramos la cédula provista
    for empleado in empleados:
        if empleado['cedula'] == cedula:
            results.append(empleado)
    # Si la cédula no hizo match con ningún registro entonces tira un error que el usuario entienda
    if results== [] :
        return "Error: La cédula provista no fue encontrada."

    # Usamos la función jsonify de Flask para convertir nuestra lista de
    # dictionarios de Python a formato JSON (generalmente los web services devuelven JSON o XML
    return jsonify(results)

#con esta instrucción "levantamos" nuestro humilde web service
app.run()
