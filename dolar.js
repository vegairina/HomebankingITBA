const list = document.getElementById("list-group")
 
fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then((data) => data.json()) /*busca info y la manda en data , no necesita usar el return ni function */
    .then((data) => 
        data.forEach(e => {
        console.log(e);
        const li = document.createElement("li");
        li.classList.add("list-group-item");
        li.innerText = `${e.casa.nombre}`;
        list.appendChild(li);

        const p =document.createElement("p");
        p.innerText = `Compra: $${e.casa.compra} - Venta: $${e.casa.venta}`;
        li.appendChild(p);
    
        })
    
    );
            
            
        

/*
let a = 5
let b = 15
function(){
    return a+b
}    
dos formas de escribir una funcion 
()=> a+b  */

