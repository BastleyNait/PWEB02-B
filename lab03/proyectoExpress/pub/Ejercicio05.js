function generar() {
    let aux  = document.querySelector("#filas");
    let numFilas = parseInt(aux.value);
    let tabla = document.getElementById("tabla");
    for(let i = 0; i < numFilas; i++) {
        document.getElementById("tabla").innerHTML += `
            <tr>
                <td>
                    <input type="text" id ="${i}" placeholder="ingrese un numero">
                </td>
            </tr>
        `;
    }

    document.getElementById("tabla").innerHTML += `
        <button onclick = "sumar()">Sumar!</button>
    `
    let generar = document.getElementById("generar");
    generar.style = "display: none";
}

function sumar() {
    let aux  = document.querySelector("#filas");
    let numFilas = parseInt(aux.value);
    let total = 0;
    for(let i = 0; i < numFilas; i++) {
        total += parseInt(document.getElementById(`${i}`).value);
    }
    document.getElementById("suma").innerHTML = `La suma es: ${total}`;
}