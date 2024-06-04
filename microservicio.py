from conexion import *

from flask import Flask, request
from flask_cors import CORS

programa = Flask(__name__)
CORS(programa)


@programa.route("/peticion_prueba", methods=['POST'])
def busca_usuario():
    nombre = request.get_json().get('usuario')

    if len(nombre) >= 6 & len(nombre) <= 15:
        sentencia = f"SELECT usuarios 'estado' FROM 'usuario' WHERE 'documento' = '{nombre}'"

        vigilante = conexion.cursor()

        vigilante.execute(sentencia)

        respuesta_servidor = vigilante.fetchall()

        microrespuesta = {
            "valor":respuesta_servidor
        }

         

    else:

        microrespuesta = {"valor":"NO"}
        return microrespuesta
    
