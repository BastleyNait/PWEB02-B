<!DOCTYPE html>
<html>
<body>

<p id = "texto">hola mundo</p>
<button onclick = 'invertir()'>Invierteme!</button> 

<p id="demo"></p>

<script>
const texto = document.querySelector("#texto");

function invertir () {
    let txt = "";
    let contador = string.length - 1;
    while(contador >= 0) {
        txt += string[contador];
        contador--;
    }
    return txt;
}

</script>

</body>
</html>

