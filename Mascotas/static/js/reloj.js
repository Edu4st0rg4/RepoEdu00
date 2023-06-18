function reloj(){
    var fecha = new Date();
    var hora = fecha.getHours(),ampm;
    var min = fecha.getMinutes();
    var seg = fecha.getSeconds();
    var actualizar = setTimeout('reloj()',500);
    
    if (hora >=12){
        hora=hora-12;
        ampm = 'PM';
    }else{
        ampm = 'AM';
    };
    if(hora==0){
        hora=12;
    };
    if(hora<10){
        hora="0"+hora
    };
    if(min<10){
        min="0"+min
    };
    if(seg<10){
        seg="0"+seg
    };
    document.getElementById('pantalla').innerHTML = hora+":"+min+":"+seg+" "+ampm;
    /*document.getElementById('pantalla').innerHTML = "25"+":"+"25"+":"+"25"+" "+ampm;*/

}   
