from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'formufront'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

@app.route('/')
def mostrar_formulario():
    return render_template('formulario.html')

@app.route('/pro_formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    email = request.form['email']
    telefono = request.form['telefono']
    fechnacim = request.form['fechnacim']
    sexo = request.form['sexo']

    cursor = mysql.get_db().cursor()
    cursor.execute("INSERT INTO formulario (nombre, apellidos, email, telefono, fechnacim, sexo) VALUES (%s, %s, %s, %s, %s, %s)",
                   (nombre, apellidos, email, telefono, fechnacim, sexo))
    mysql.get_db().commit()
    cursor.close()

    return "Datos registrados."

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)












'''
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

formulario = Flask(__name__)

formulario.config['MYSQL_DATABASE_USER'] = 'root'
formulario.config['MYSQL_DATABASE_PASSWORD'] = ''
formulario.config['MYSQL_DATABASE_PORT'] = 3306
formulario.config['MYSQL_DATABASE_DB'] = 'fromufront'
formulario.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(formulario)

@formulario.route('/')
def mostrar_formulario():
    return render_template('formulario.html')

@formulario.route('/pro_formulario', methods=['POST'])
def pro_formulario():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    email = request.form['email']
    telefono = request.form['telefono']
    fechnacim = request.form['fechnacim']
    sexo = request.form['sexo']

    cursor = mysql.connect.cursor()
    cursor.execute("INSERT INTO formulario (nombre, apellidos, email, telefono, fechnacim, sexo) VALUES (%s, %s, %s, %s, %s, %s)"\
                   (nombre, apellidos, email, telefono, fechnacim, sexo))
    mysql.connect.commit()
    cursor.close()

    return "Datos registrados."

if __name__ == '__main__':
    formulario.run(host='0.0.0.0', debug= True, port= 3306)

'''