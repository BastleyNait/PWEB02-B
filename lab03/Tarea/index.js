const express = require('express')
const app = express()
const port = 3000
const fs = require("fs")
const { join } = require('path')
app.use(express.static('pub'))
app.use(express.json())

app.listen(port, () => console.log(`Example app listening on port http://localhost:${port}`))

app.get('/', (request, response) => {
  response.sendFile('index.html', {
    root: __dirname
  })
})

app.get('/titulos', (req, res) => {
  let datos = [];
  const contenido = fs.readFileSync('datos.json', 'utf-8');
  datos = JSON.parse(contenido);
  const titulos = datos.map((objeto) => objeto.titulo);
  console.log(titulos);
  res.json(titulos);
});
app.get('/ver/:titulo', (req, res) => {
  let datos = [];
  const contenido = fs.readFileSync('datos.json', 'utf-8');
  datos = JSON.parse(contenido);
  datos.forEach((objeto) => {
    if(objeto.titulo == req.params.titulo) {
      texto = {
        contenido: objeto.contenido
      };
    }
  })
  console.log(texto);
  res.json(texto);
});

app.post('/ver/:titulo', (req, res) => {
  let datos = [];
  const contenido = fs.readFileSync('datos.json', 'utf-8');
  datos = JSON.parse(contenido);
  datos.forEach((objeto) => {
    if(objeto.titulo == req.params.titulo) {
      texto = {
        contenido: objeto.contenido
      };
    }
  })
  console.log(texto);
  res.json(texto);
});

app.put('/editar/:titulo', (req, res) => {
  let datos = [];
  const contenido = fs.readFileSync('datos.json', 'utf-8');
  datos = JSON.parse(contenido);
  datos.forEach((objeto) => {
    if(objeto.titulo == req.params.titulo) {
      texto = {
        contenido: objeto.contenido
      };
    }
  })
  console.log(texto);
  res.json(texto);
});

app.delete('/editar/:titulo', (req, res) => {
  let datos = [];
  const contenido = fs.readFileSync('datos.json', 'utf-8');
  datos = JSON.parse(contenido);
  datos = datos.filter((objeto) => objeto.titulo != req.params.titulo);
  fs.writeFileSync('datos.json', JSON.stringify(datos), 'utf-8');
  console.log(datos)
  res.json({
    message:"el archivo ha sido eliminado"
  });
});
