#los templates son las vistas o pestañas de

from flask import * #para importar las cosas de una libreria

#Crear una instancia de la clase flsk


#Definir rutas
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#@app.route <-Esto sirve para crear una ruta nueva
@app.route('/Saludo')  #lo de adentro de los parentesis es la dirección de la web
def Saludo():
    return"Creando rutas al pryoecto"

@app.route('/Registrar')
def Registrar():
    return render_template('Registrar.html')


#Se ejecuta la app o el servidor
if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True,port=5005)


