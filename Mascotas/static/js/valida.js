
//función que valida un formulario
 $(function(){
    $("#datos").validate({
        rules:{
            nom:{
                required:true
            },
            ape:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },

            fono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            }
        },//rules
        messages:{
            nom:{
                required:'Ingrese nombre de usuario',
                minlength:'Formato incorrecto de nombre (3)'
            },
            ape:{
                required:'Ingrese apellido de usuario',
                minlength:'Formato incorrecto de nombre (3)'
            },
            correo:{
                required:'Ingrese correo de usuario',
                email: 'Formato de correo inválido'
            },
            fono:{
                required: 'Ingrese teléfono',
                minlength:'Cantidad de digitos insuficientes(9)'
            },
            fecha:{
                required:'Seleccione una fecha válida',
                min:'Fecha incorrecta'
            },
            motivo:{
                required:'Debe seleccionar un motivo'
            }

        },//messages                
    })
});

function colorOrange(obj){
    obj.style.backgroundColor='orange';
}
function colorBlanco(obj){
    obj.style.backgroundColor='white';
}

function upperText(texto)
{
    const x = texto;
    x.value= x.value.toUpperCase();
}

function colorFondo(obj){
    obj.style.backgroundColor='pink';
}

function Mostrar(datos) {
    //variables generales
    var nom = document.getElementById("nom").value;
    var ape = document.getElementById("ape").value;
    var correo = document.getElementById("correo").value;
    var fono = document.getElementById("fono").value;
    var fecha = document.getElementById("fecha").value;
    var motivo = parseInt(document.getElementById("motivo").value);

    //variables genero
    var elementoMotivo = document.getElementById("motivo");
    var indiceSeleccionado = elementoMotivo.selectedIndex;
    var motivo = elementoMotivo.options[indiceSeleccionado].text;
  
    //compilado datos en text area
    datos = ("Sus datos son: " +
      "\nNombre: " + nom +
      "\nApellido: " + ape +
      "\nCorreo: " + correo +
      "\nFono: " + fono +
      "\nFecha de nacimiento: " + fecha +
      "\motivo: " + motivo);
  
    // Mostrar los datos en un mensaje de alerta
    alert("Mensaje enviado con el siguiente contenido/n"+datos);
  }
  function Saludar(){
    alert("Mensaje enviado con el siguiente contenido/n"+datos);
}

function clickMeEvent(obj) {
    if (obj.innerHTML == "Todo Perros") {
    obj.innerHTML = "Hola profe :3";
    return;
    }
    if (obj.innerHTML == "Hola profe :3") {
    obj.innerHTML = "Todo Perros";  
    return; 
    }
}

function clickMeEvent1(obj) {
    if (obj.innerHTML == "Todo Gatos") {
      obj.innerHTML = "Miau";
      return;
    }
    if (obj.innerHTML == "Miau") {
      obj.innerHTML = "Todo Gatos";  
      return; 
    }
}

function clickMeEvent2(obj) {
    if (obj.innerHTML == "Todo Exóticos") {
      obj.innerHTML = "Holiwi";
      return;
    }
    if (obj.innerHTML == "Holiwi") {
      obj.innerHTML = "Todo Exóticos";  
      return; 
    }
}

function colors(obj){
    obj.style.backgroundColor='lightgrey';
}
function colorBlanco(obj){
    obj.style.backgroundColor='white';
}

function upperText(texto)
{
    const x = texto;
    x.value= x.value.toUpperCase();
}

function colorFondo(obj){
    obj.style.backgroundColor='pink';
}