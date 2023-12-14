from flask import Flask, render_template, request

app = Flask(__name__)

def validar_reserva(campo_identificador):
    # Verificación para una reserva   SANTIAGO VELEZ CEDULA
    if (
        len(campo_identificador) == 6 and
        campo_identificador[0].isalpha() and
        campo_identificador[1:4].isdigit() and
        campo_identificador[4:6].isalpha() and
        'A' <= campo_identificador[4].upper() <= 'F'
    ):
        return True
    
    # Verificación para una cedula 
    elif len(campo_identificador) <= 10 and campo_identificador.isdigit():
        return True
    
    # Verificación para pasaporte
    elif (
        len(campo_identificador) == 8 and
        campo_identificador[0] == 'A' and
        campo_identificador[1].isalpha() and
        campo_identificador[2:].isdigit()
    ):
        return True
    
    # Verificación para cedula de extranjeria
    elif len(campo_identificador) == 7 and campo_identificador.isdigit():
        return True
    
    # Verificación para PEP
    elif len(campo_identificador) == 15 and campo_identificador.isdigit():
        return True 

    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscarReserva', methods=['POST'])
def validar_reserva_route():
    reserva = request.form.get('campo_identificador')

    # Realiza la validación según tus reglas
    es_valido = validar_reserva(reserva)

    if es_valido:
        mensaje_reserva = "¡Correcto! El formato es válido."
    else:
        mensaje_reserva = "Error: El formato no es válido."

    return render_template('index.html', mensaje_reserva=mensaje_reserva)

if __name__ == '__main__':
    app.run(debug=True)
