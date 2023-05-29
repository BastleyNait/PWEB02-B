const express = require('express')
const app = express()
const MarkdownIt = require('markdown-it')
const md = new MarkdownIt()
const port = 3000
const fs = require("fs")
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
    console.log(req.params.titulo);
  })
  const htmltext = {
    contenido: md.render(texto.contenido)
  };
  console.log(htmltext);
  res.json(htmltext);
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

app.post('/crear', (req, res) => {
  let datos = [];
  const contenido = fs.readFileSync('datos.json', 'utf-8');
  datos = JSON.parse(contenido);
  console.log(req.body);
  datos.push(req.body);
  fs.writeFileSync('datos.json', JSON.stringify(datos), 'utf-8');
  res.json({
    message:"texto guardado con exito"
  })
})

app.patch('/editar/:titulo', (req, res) => {
  let datos = [];
  const contenido = fs.readFileSync('datos.json', 'utf-8');
  datos = JSON.parse(contenido);
  datos = datos.filter((objeto) => objeto.titulo != req.params.titulo);
  console.log("bañate");
  datos.push(req.body);
  fs.writeFileSync('datos.json', JSON.stringify(datos), 'utf-8');
  res.json({
    message:"se guardó con exito"
  })
})