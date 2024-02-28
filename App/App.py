#los templates son las vistas o pestañas de

from flask import * #para importar las cosas de una libreria
import mysql.connector #importamos el SQL

#configurar conexción
db =mysql.connector.connect(
    host="localhost", #valor por default
    user="root",
    pasword="",
    database="agenda2024"
)
cursor =db.cursor() #es la connxión 


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

@app.route('/Registrar', methods=['POST'])
def Registrar():

    Nombres =request.form['name'],
    Apellidos= request.form['apellido']
    usuario = request.form['usuario']
    correo = request.form['correo']
    Celular = request.form['celular']
    dirección= request.form['direccion']
    contraseña= request.form['contrasena']
    
    #insertar datos en la tabla
    cursor.execute("INSERT INTO Personas (Nombre_persona, Apellido_persona, Nombre_usuario, correo, celular, dirección, contraseña) VALUES(%s, %s, %s, %s, %s, %s, %s,)",(Nombres, Apellidos, usuario, correo, Celular, dirección, contraseña,) )
    db.commit()
    
    return redirect(url_for('Registrar'))






#Se ejecuta la app o el servidor
if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True,port=5005)


