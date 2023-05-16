<!DOCTYPE html>
<html>
<body>

<p id="texto">hola mundo</p>
<button onclick='invertir()'>Inviérteme!</button> 

<p id="demo"></p>

<script>
const texto = document.querySelector("#texto").textContent;

function invertir() {
    let txt = "";
    let contador = texto.length - 1;
    while (contador >= 0) {
        txt += texto[contador];
        contador--;
    }
    document.querySelector("#demo").innerHTML = txt;
}
</script>

</body>
</html>
