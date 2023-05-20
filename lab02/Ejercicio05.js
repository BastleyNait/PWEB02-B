function generar() {
    let aux  = document.querySelector("#filas");
    let numFilas = parseInt(aux.value);
    let tabla = document.getElementById("tabla");
    for(let i = 0; i < numFilas; i++) {
        document.getElementById("tabla").innerHTML += `
            <tr>
                <td>
                    <input type="number" id ="${i}" placeholder="ingrese un numero">
                </td>
            </tr>
        `;
    }

    document.getElementById("tabla").innerHTML += `
        <button onclick = "sumar()">Sumar!</button>
    `
}

function sumar() {
    let aux  = document.querySelector("#filas");
    let numFilas = parseInt(aux.value);
    let total = 0;
    for(let i = 0; i < numFilas; i++) {
        total += parseInt(document.getElementById(`${i}`).value);
    }
    if(!isNaN(total)) {
        document.getElementById("suma").innerHTML = `La suma es: ${total}`;
    } else {
        document.getElementById("suma").innerHTML = `por favor, numeros`;
    }

}
