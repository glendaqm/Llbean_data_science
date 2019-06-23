from flask import Flask, json
from flask_restful import Api, Resource, reqparse

#Creates the Flask application object, which contains data about the application and also methods (object functions)
# that tell the application to do certain actions. The last line, app.run(), is one such method.
app = Flask(__name__)
api = Api(app)

empleados = [
    {
        "cedula": "110870778",
        "nombre": "Glenda",
        "apellido1": "Quesada",
        "apellido2": "Monge",
        "fecha ingreso": "21 de Agosto del 2006",
        "puesto": "IS Manager III",
        "departamento":"Information Services",
        "salarioBruto":"300,000"
    },
    {
        "cedula": "110001000",
        "nombre": "Juan",
        "apellido1": "Perez",
        "apellido2": "Perez",
        "fecha ingreso":"10 de Noviembre del 2002",
        "puesto": "Sr. Programmer",
        "departamento":"Information Services",
        "salarioBruto":"200,000"
    },
    {
        "cedula": "900010783",
        "nombre": "Julia",
        "apellido1": "Monge",
        "apellido2": "Quesada",
        "fecha ingreso":"16 de Junio del 2019",
        "puesto": "Asistente Administrativa",
        "departamento":"Recursos Humanos",
        "salarioBruto":"100,000"
    },
    {
        "cedula": "110250162",
        "nombre": "Esteban",
        "apellido1": "Chavarria",
        "apellido2": "Vega",
        "fecha ingreso":"13 de Mayo del 2019",
        "puesto": "Sourcing Manager",
        "departamento":"Global Procurement",
        "salarioBruto":"500,000"
    }
]

class Empleado(Resource):

    #def __init__(self, ced):
        #self.ced = ced


    def get(self, cedula):
        for empleado in empleados:
            if(cedula == empleado["cedula"]):
                #converts from Python to JSON
                json_data = json.dumps(empleado)
                return json_data, 200
                #return empleado, 200
                #return jsonify(empleado), 200
        return "Empleado no encontrado", 404


api.add_resource(Empleado, "/user/<string:cedula>")

#add_resource(resource, *urls, **kwargs)
#Adds a resource to the api.

#Parameters:
#resource (Type[Resource]) – the class name of your resource
#urls (str) – one or more url routes to match for the resource, standard flask routing rules apply. Any url variables will be passed to the resource method as args.
#endpoint (str) – endpoint name (defaults to Resource.__name__.lower() Can be used to reference this route in fields.Url fields
#resource_class_args (tuple) – args to be forwarded to the constructor of the resource.
#resource_class_kwargs (dict) – kwargs to be forwarded to the constructor of the resource.

#A method that runs the application server. Debug= True: if your code is malformed, you’ll see an error when you visit your app
app.run(debug=True)