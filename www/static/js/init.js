
// // Script para actualizacion de las muestras segun la frecuencia elegida
//   var counter = 0;
//   var idInter=-1; 
 
//             // Funcion para tomar la frecuencia
//            window.onload=function(){
//              document.getElementById("nuevobutton").addEventListener("click",function ()
//             {
//                 var x = document.getElementById("frec");
//                 // var strUser = x.options[x.selectedIndex].value;
//                 var interval = 5000;
//                 console.log(idInter);
//               //  $("#cartel").text("Actualizando cada "+ strUser + " segundos")  
//                 if (idInter != -1){ 
//                     window.clearInterval(idInter); 
//                 }
//                 // var interval = strUser*1000;
//                 idInter = window.setInterval('refreshDiv()', interval);
//             } );
//          }
//             // Funcion para refrescar el Div
//             function refreshDiv(){
//                 counter = counter + 1;
//                 console.log(counter);
//                  $.get("/eventsjson/",cors function(data) {
//                 // $("#id").text(data.id);
//                 // for (const prop in data){

//                   $("#idfecha").text(data[0][2].created);
//                   $("#idstate").text(data[0][2].semaphore_state);

//                 console.log(text(data[0][0].semaphore_state));       
//                 });

                
//             }