fetch('/titulos')
  .then(response => response.json())
  .then(data => {
    const listaTitulos = document.getElementById('lista-titulos');
    data.forEach(titulo => {
      listaTitulos.innerHTML += `
        <div class='caja'>
          <li>${titulo}</li>
          <button onclick="ver(${titulo})"></button>
          <button>Editar</button>
          <button>Eliminar</button>
        </div>
      `
    });
  });

function ver(titulo) {  
  fetch(`/ver/${titulo}`)
  .then(response => response.json())
  .then(data => {
    const listaTitulos = document.getElementById('lista-titulos');
    data.forEach(titulo => {
      listaTitulos.innerHTML += `
        <div class='caja'>
          <li>${titulo}</li>
          <button onclick="ver(${titulo})"></button>
          <button>Editar</button>
          <button>Eliminar</button>
        </div>
      `
    });
  });
}
  


