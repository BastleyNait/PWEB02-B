fetch('/titulos')
  .then(response => response.json())
  .then(data => {
    const listaTitulos = document.getElementById('lista-titulos');
    data.forEach(titulo => {
      listaTitulos.innerHTML += `
        <div class='caja'>
          <li>${titulo}</li>
          <div class="botones">
            <button onclick='ver("${titulo}")'>Ver</button>
            <button onclick='editar("${titulo}")'>Editar</button>
            <button onclick='eliminar("${titulo}")'>Eliminar</button>
          </div>
          </div>
          <div class="contenidoTexto" id="contenido de ${titulo}"></div>
      `
    });
  });
//sa
function ver(titulo) {  
  fetch(`/ver/${titulo}`)
  .then(response => response.json())
  .then(data => {
    console.log(data.contenido);
    document.getElementById(`contenido de ${titulo}`).innerHTML = data.contenido;
  });
}

function editar(titulo) {
  const request = {
    method: 'POST', 
    headers: {'Content-Type': 'application/json',},
  }   
  fetch(`/ver/${titulo}`,request)
  .then(response => response.json())
  .then(data => {   
    let texto = document.getElementById(`contenido de ${titulo}`);
    texto.innerHTML = `
    <div class="edit">
      <textarea class = "edit" id="markupText de ${titulo}" name="markupText" cols="50" rows="10">${data.contenido}</textarea><br>
      <button onclick='salvar("${titulo}")'>guardar</button>
    </div>
    `;
  });
}

function eliminar(titulo) {
  const request = {
    method: 'DELETE', 
    headers: {'Content-Type': 'application/json',},
  } 
  fetch(`/editar/${titulo}`, request)
  .then(res => res.json())
  .then(data => {
    alert(data.message)
    location.reload();
  })
}


function guardar() {
  const titulo = document.getElementById('titulo').value
  const contenido = document.getElementById('contenido').value;
  const data = {
    titulo: titulo,
    contenido: contenido
  }
  const req = {
    method: "POST",
    headers: {'Content-Type': 'application/json',},
    body: JSON.stringify(data)
  }

  fetch('/crear', req)
  .then(res => res.json())
  .then(data => alert(data.message))
  location.reload();
}

function nuevo() {
  const espacios = document.querySelector(".areaTexto")
  espacios.innerHTML = `
  <textarea class="nuevoTexto" name="titulo" id="titulo" cols="30" rows="1" placeholder="Titulo" required></textarea>
  <textarea class="nuevoTexto" name="contenido" id="contenido" cols="60" rows="10" placeholder="Contenido en Markdown" required></textarea>
  <button onclick="guardar()">Guardar</button>
  `
}

function salvar (titulo) {
  const contTexto = document.getElementById(`markupText de ${titulo}`).value
  let data = {
    titulo: titulo,
    contenido: contTexto
  }
  const req = {
    method: "PATCH",
    headers: {'Content-Type': 'application/json',},
    body: JSON.stringify(data)
  }
  fetch(`/editar/${titulo}`,req)
  .then(response => response.json())
  .then(data => alert(data.message))
  location.reload();
}



  


