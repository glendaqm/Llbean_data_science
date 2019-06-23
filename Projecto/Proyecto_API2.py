import flask
from flask import request, jsonify

#Creates the Flask application object, which contains data about the application and also methods (object functions) that tell the application to do certain actions.
# The last line, app.run(), is one such method.
app = flask.Flask(__name__)
#Starts the debugger. With this line, if your code is malformed, you’ll see an error when you visit your app.
app.config["DEBUG"] = True


#Diccionario de empleados. En la vida real Workday lo obtendria de una base de datos
empleados = [
    {
        "cedula": 110870778,
        "nombre": "Glenda",
        "apellido1": "Quesada",
        "apellido2": "Monge",
        "fecha_ingreso": "21 de Agosto del 2006",
        "puesto": "IS Manager III",
        "departamento":"Information Services",
        "salarioBruto":"300,000"
    },
    {
        "cedula": 110001000,
        "nombre": "Juan",
        "apellido1": "Perez",
        "apellido2": "Perez",
        "fecha_ingreso":"10 de Noviembre del 2002",
        "puesto": "Sr. Programmer",
        "departamento":"Information Services",
        "salarioBruto":"200,000"
    },
    {
        "cedula": 900010783,
        "nombre": "Julia",
        "apellido1": "Monge",
        "apellido2": "Quesada",
        "fecha_ingreso":"16 de Junio del 2019",
        "puesto": "Asistente Administrativa",
        "departamento":"Recursos Humanos",
        "salarioBruto":"100,000"
    },
    {
        "cedula": 110250162,
        "nombre": "Esteban",
        "apellido1": "Chavarria",
        "apellido2": "Vega",
        "fecha_ingreso":"13 de Mayo del 2019",
        "puesto": "Sourcing Manager",
        "departamento":"Global Procurement",
        "salarioBruto":"500,000"
    }
]

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>El recurso no pudo ser encontrado.</p>", 404


#The process of mapping URLs to functions is called routing. The @app.route('/', methods=['GET']) syntax is the part
# of the program that lets Flask know that this function, home, should be mapped to the path /.
# The methods list (methods=['GET']) is a keyword argument that lets Flask know what kind of HTTP requests are allowed.

@app.route('/api/v1/resources/emp', methods=['GET'])
def api_empleado():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'cedula' in request.args:
        cedula = int(request.args['cedula'])
    else:
        return "Error: La cédula no fue provista. Por favor especifique una."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for empleado in empleados:
        if empleado['cedula'] == cedula:
            results.append(empleado)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()
