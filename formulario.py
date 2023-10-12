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

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO formulario (nombre, apellidos, email, telefono, fechnacim, sexo) VALUES (%s, %s, %s, %s, %s, %s)"\
                   (nombre, apellidos, email, telefono, fechnacim, sexo))
    mysql.connectionn.commit()
    cursor.close()

    return "Datos registrados."

if __name__ == '__main__':
    formulario.run(host='0.0.0.0', debug= True, port= 3306)