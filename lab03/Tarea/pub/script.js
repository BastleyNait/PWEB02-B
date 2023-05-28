fetch('/titulos')
  .then(response => response.json())
  .then(data => {
    const listaTitulos = document.getElementById('lista-titulos');
    data.forEach(titulo => {
      listaTitulos.innerHTML += `
        <div class='caja'>
          <li>${titulo}</li>
          <button onclick='ver("${titulo}")'>Ver</button>
          <button onclick='editar("${titulo}")'>Editar</button>
          <button>Eliminar</button>
        </div>
        <div id="contenido de ${titulo}"></div>
      `
    });
  });
//sa
function ver(titulo) {  
  fetch(`/ver/${titulo}`)
  .then(response => response.json())
  .then(data => {
    document.getElementById(`contenido de ${titulo}`).innerHTML = data.contenido;
  });
}

function editar(titulo) {  
  fetch(`/ver/${titulo}`)
  .then(response => response.json())
  .then(data => {   
    let texto = document.getElementById(`contenido de ${titulo}`);
    texto.innerHTML = `
    <textarea id="markupText" name="markupText">${data.contenido}</textarea><br>
    `;
  });
}





  


