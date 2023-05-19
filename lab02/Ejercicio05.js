function generar() {
    let aux  = document.querySelector("#filas");
    let numFilas = parseInt(aux.value);
    const contenedor = document.getElementById("contenedor");
    let table = document.createElement("table");
    contenedor.appendChild(table);

    for(let i = 0; i < numFilas; i++) {
        let tr = document.createElement("tr");
        let td = document.createElement("td");
        let input = document.createElement("input");
        

    }
}