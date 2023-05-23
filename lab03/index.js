const http = require("http");
const server = http.createServer((req, res) => {
    res.end("Hola Mundo");
});
server.listen(3000);
console.log("escuchando en http://localhost:3000")