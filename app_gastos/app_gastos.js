(function(){ 
    var lista = document.getElementById("lista"),
        nombreInput = document.getElementById("nombreInput"),
        montoInput = document.getElementById("montoInput"),
        btnNuevaPersona = document.getElementById("btn-agregar"),
        contador = 0,
        total = 0,
        promedio = 0;
        
        


    var agregarPersona = function(){
        var nombre = nombreInput.value,
            monto = montoInput.value;
            nuevoItem = document.createElement("li"),
            enlace = document.createElement("a"),
            contenido = document.createTextNode(nombre+" $ " + monto),
            br = document.createElement("br");


    
        if(nombre === ""){
            nombreInput.setAttribute("placeholder","Agregar Nombre válido");
            nombre.className="Error";
            return false;
        }

        if(monto === ""){
            montoInput.setAttribute("placeholder","Agregar Monto válido");
            nombre.className="Error";
            return false;
        }

        enlace.appendChild(contenido);
        enlace.setAttribute("href","#");
        nuevoItem.appendChild(enlace);
        lista.appendChild(nuevoItem);
        contador ++;
        total = parseFloat(monto) + total;
        document.getElementById('total').innerHTML = total;
        promedio = total/contador;
        document.getElementById('promedio').innerHTML = promedio;




        nombreInput.value ="";



    };

    var comprobarInput = function(){
        nombreInput.className="";
        nombreInput.setAttribute("placeholder","Ingrese su Nombre");
    };


    btnNuevaPersona.addEventListener("click", agregarPersona);
    nombreInput.addEventListener("click", comprobarInput);


    
}())