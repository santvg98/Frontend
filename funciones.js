async function validarUsuario (valor) {

    console.log(valor)

    try {

        var datos = {
            usuario: valor,
    
        };

        var servidor = "http://10.206.80.86:5080/peticion_prueba";

        var parametros = {
            method: "POST",
            body: JSON.stringify(datos),
            headers: {
                "content-type":"application/json"
            }, 
        };

        const response = await fetch(servidor, parametros);

        var respuesta_servidor = await response.json();

        console.log("Servidor respondió: ", respuesta_servidor);



    } catch (error) { //lo que sucede si hay error en la ejecución
        console.error("Hubo un error en: ", error);

    }

    

    
    
}


document.addEventListener("DOMContentLoaded", () => {
    if(document.getElementById('nom_usuario')) {

        let nom_usuario = document.getElementById('nom_usuario');

        nom_usuario.addEventListener("keyup", (campo) => {
            let digitado = campo.target.value;

            if(digitado.length >= 6 && digitado.length <= 15) {
                validarUsuario(digitado);
            }
        });
    }
});

