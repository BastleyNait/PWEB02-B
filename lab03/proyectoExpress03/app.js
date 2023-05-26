const path = require('path')
const express = require('express')
const bp = require('body-parser')
const MarkdownIt = require('markdown-it')
const md = new MarkdownIt()
const app = express()

app.use(express.static('pub'))
app.use(bp.json())
app.use(bp.urlencoded({
    extended: true
}))

app.listen(4000, () => {
    console.log("Escuchando en: http://localhost:4000")
})

app.get('/', (request, response) => {
    response.sendFile(path.resolve(__dirname, 'index.html'))
})

app.post('/', (request, response) => {
    try {
        let markDownText = request.body.text
        console.log(markDownText)
        let htmlText = md.render(markDownText)
        response.setHeader('Content-Type', 'application/json')
        response.end(JSON.stringify({
            text: htmlText
        }))
    } catch (error) {
        console.error(error)
        response.status(500).send('An error occurred')
    }
})
