
<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2023/03/01</td><td colspan="2"><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td></tr>
    </tbody>
</table>
</div>

<div align="center">
</div>
<div align="center">
	<span style="font-weight:bold;">INFORME DE LABORATORIO</span>

<table>
		<theader>
			<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
		</theader>
		<tbody>
			<tr>
				<td><span style="font-weight:bold;">ASIGNATURA:</span></td>
				<td colspan="5">Programación Web II</td>
			</tr>
			<tr>
				<td><span style="font-weight:bold;">TÍTULO DE LA PRÁCTICA:<span></td>
				<td colspan="5">Ajax y NodeJs</td>
			</tr>
			<tr>
				<td>NÚMERO DE PRÁCTICA:</td>
				<td>03</td><td>AÑO LECTIVO:</td>
				<td>2023 A</td>
				<td>NRO. SEMESTRE:</td>
				<td>III</td>
			</tr>
			<tr>
				<td>FECHA DE PRESENTACIÓN::</td>
				<td>29-May-2022</td>
				<td>HORA DE PRESENTACIÓN:</td>
				<td> 10:00 pm.</td>
			</tr>
			<tr>
				<td colspan="3">ALUMNO:
					<ul>
				    <li>Chirinos Negron Sebastian Arley</li>
					</ul>
				</td>
				<td colspan="">NOTA:</td>
				<td></td>
			</tr>
			<tr>
				<td colspan="6">DOCENTE:
					<ul>
					<li>Anibal Sardon</li>
					</ul>
				</td>
			</tr>
		</tdbody>
</table>
</div>
	
<div align="center"><h2> SOLUCIÓN Y RESULTADOS </h2></div>	

### I.	SOLUCIÓN DE EJERCICIOS/PROBLEMAS
	
**LINK REPOSITORIO: [https://github.com/BastleyNait/PWEB02-B.git](https://github.com/GonzaloRail/Laboratorio_03_PWEB2_GRUPAL.git)**
  
-   
    
-   El Framework Express basado en NodeJS para el BackEnd
   
-   Los archivos se guardaron en Sistema de Archivos del Sistema Operativo del Servidor a través de la dependencia nativa File System (fs).
    
-   JavaScript para el FrontEnd
    
-   Las páginas se escriben en lenguaje Markdown
    
-   Se utilizó la dependencia markdown-it
    
-   La comunicación entre el Cliente y el Servidor se hizo usando JSON de manera asíncrona.

**Iniciando proyecto Express**

```sh
     npm init
```

**Install dependencies**

```sh
     npm install express
     npm install markdown-it
     npm install nodemon
```

-   **Servidor**
    

En este bloque de código, se importan las dependencias necesarias: `express` para crear el servidor web, `MarkdownIt` para convertir Markdown a HTML y `fs` para leer y escribir archivos. Luego, se crea una instancia de la aplicación Express y se configura para utilizar archivos estáticos en la carpeta "pub" y analizar el cuerpo de las solicitudes en formato JSON. Por último, se inicia el servidor en el puerto 3000 y se muestra un mensaje en la consola indicando que la aplicación está escuchando.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20230251.png?raw=true">

Este bloque de código maneja la solicitud GET a la ruta raíz ("/"). Cuando se recibe esta solicitud, se envía el archivo "index.html" al cliente desde la carpeta actual (__dirname).
En este bloque de código, se maneja la solicitud GET a la ruta "/titulos". Se lee el contenido del archivo "datos.json" y se parsea a un objeto JavaScript. Luego, se crea un nuevo arreglo llamado `titulos` mediante el mapeo de los objetos en `datos`, extrayendo solo la propiedad "titulo". Este arreglo de títulos se envía como respuesta al cliente en formato JSON.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20230304.png?raw=true">

En este bloque de código, se maneja la solicitud GET a la ruta "/ver/:titulo", donde ":titulo" es un parámetro dinámico que indica el título del objeto que se desea ver. Se lee el contenido del archivo "datos.json" y se parsea a un objeto JavaScript. Luego, se recorre el arreglo `datos` y se busca un objeto con el título que coincide con el parámetro recibido. Si se encuentra, se asigna su contenido a la variable `texto`. Luego, se utiliza la instancia de `MarkdownIt` para renderizar el contenido en formato Markdown a HTML, y se guarda en `htmltext`. Finalmente, se envía el HTML generado como respuesta al cliente.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20230317.png?raw=true">
En este bloque de código, se maneja la solicitud POST a la ruta "/ver/:titulo". Se lee el contenido del archivo "datos.json" y se parsea a un objeto JavaScript. Luego, se recorre el arreglo `datos` y se busca un objeto con el título que coincide con el parámetro recibido. Si se encuentra, se asigna su contenido a la variable `texto`. Finalmente, se envía el objeto `texto` como respuesta al cliente en formato JSON.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20230317.png?raw=true">
contenido en formato Markdown a HTML, y se guarda en `htmltext`. Finalmente, se envía el HTML generado como respuesta al cliente.
En este bloque de código, se maneja la solicitud PUT a la ruta "/editar/:titulo". Se lee el contenido del archivo "datos.json" y se parsea a un objeto JavaScript. Luego, se recorre el arreglo `datos` y se busca un objeto con el título que coincide con el parámetro recibido. Si se encuentra, se asigna su contenido a la variable `texto`. Finalmente, se envía el objeto `texto` como respuesta al cliente en formato JSON.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20230325.png?raw=true">
En este bloque de código, se maneja la solicitud DELETE a la ruta "/editar/:titulo". Se lee el contenido del archivo "datos.json" y se parsea a un objeto JavaScript. Luego, se filtra el arreglo `datos` para eliminar el objeto cuyo título coincide con el parámetro recibido. Después de eso, se escribe el nuevo arreglo `datos` en el archivo "datos.json". Finalmente, se envía una respuesta JSON con un mensaje indicando que el archivo ha sido eliminado.
Este bloque de código maneja la solicitud POST a la ruta '/crear'. Primero, se lee el contenido del archivo 'datos.json' y se parsea a un objeto JavaScript llamado `datos`. Luego, se obtiene el cuerpo de la solicitud (req.body) que contiene un nuevo objeto de datos a ser agregado. Este nuevo objeto se añade al arreglo `datos` utilizando el método `push()`. Después, se escribe el nuevo arreglo `datos` en el archivo 'datos.json' utilizando `fs.writeFileSync()`. Finalmente, se envía una respuesta JSON con un mensaje indicando que el texto se guardó exitosamente.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20230340.png?raw=true">
Este bloque de código maneja la solicitud PATCH a la ruta '/editar/:titulo'. Primero, se lee el contenido del archivo 'datos.json' y se parsea a un objeto JavaScript llamado `datos`. Luego, se realiza un filtrado en el arreglo `datos` utilizando el método `filter()`. Se eliminan todos los objetos que tengan un título igual al parámetro recibido (req.params.titulo). Después, se añade el nuevo objeto de datos (req.body) al arreglo `datos` utilizando `push()`. Luego, se escribe el nuevo arreglo `datos` en el archivo 'datos.json'. Finalmente, se envía una respuesta JSON con un mensaje indicando que los cambios se guardaron exitosamente.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20230350.png?raw=true">
- **Cliente script.js**
Este bloque de código realiza una solicitud GET a la ruta '/titulos' utilizando `fetch()`. Luego, convierte la respuesta en formato JSON utilizando el método `response.json()`. Después de eso, manipula los datos obtenidos en la respuesta.

Dentro del segundo `then()`, se realiza un bucle `forEach` en los datos recibidos, que son los títulos obtenidos del servidor. Para cada título, se agrega una estructura HTML al elemento con el id 'lista-titulos'. Esta estructura consiste en un div con la clase 'caja', que contiene un elemento de lista 'li' con el título. Además, se incluye un conjunto de botones para ver, editar y eliminar, cada uno con un evento `onclick` que llama a las funciones correspondientes. Por último, se agrega un div con la clase 'contenidoTexto' y un id único basado en el título.
Esta función `ver(titulo)` se invoca cuando se hace clic en el botón "Ver". Realiza una solicitud GET a la ruta `/ver/${titulo}` para obtener el contenido de un título específico. Luego, convierte la respuesta en formato JSON y asigna el contenido al div con el id único correspondiente.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20231242.png?raw=true">
La función `editar(titulo)` se llama al hacer clic en el botón "Editar". Envia una solicitud POST a la ruta `/ver/${titulo}` para obtener el contenido de un título específico. Luego, convierte la respuesta en formato JSON y muestra un área de texto dentro del div con el id único correspondiente, que permite al usuario editar el contenido. Al hacer clic en el botón "Guardar", se llama a la función `salvar(titulo)`.
La función `eliminar(titulo)` se ejecuta cuando se hace clic en el botón "Eliminar". Realiza una solicitud DELETE a la ruta `/editar/${titulo}` para eliminar un título específico. Después de recibir la respuesta en formato JSON, muestra una alerta con el mensaje de respuesta y recarga la página.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20231304.png?raw=true">
La función `guardar()` se llama cuando se hace clic en el botón "Guardar" al crear un nuevo título. Obtiene los valores del título y contenido del formulario y los guarda en un objeto `data`. Luego, crea una solicitud POST a la ruta '/crear' con los datos en formato JSON. Después de recibir la respuesta en formato JSON, muestra una alerta con el mensaje de respuesta y recarga la página.
La función `nuevo()` se llama cuando se hace clic en el botón "Nuevo". Reemplaza el contenido del elemento con la clase 'areaTexto' con un formulario que permite al usuario ingresar un nuevo título y contenido en formato Markdown, y tiene un botón "Guardar" que llama a la función `guardar()`.
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20231312.png?raw=true">
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20231317.png?raw=truee">
- **Cliente index.html y css**
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20231822.png?raw=true">
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/masimages/Captura%20de%20pantalla%202023-05-29%20231855.png?raw=true">
#	
- **Ejecución:**
Acá se muestra la lista inicial de documentos que ya existen en el servidor:
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/lab03/Captura%20de%20pantalla%202023-05-29%20225033.png?raw=true">

Hacemos click en la opcion nuevo documento para crear un nuevo texto en markdown:  

<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/lab03/Captura%20de%20pantalla%202023-05-29%20225059.png?raw=true">    

Ponemos el título y el contenido a nuestro documento y seguidamente lo guardamos:

<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/lab03/Captura%20de%20pantalla%202023-05-29%20225224.png?raw=true">
 
y nos manda una ventana emergente en la cual nos confirma que se ha guardado correctamente:

<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/lab03/Captura%20de%20pantalla%202023-05-29%20225232.png?raw=true">

Y como podemos ver se actualizó la lista automáticamente:

<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/lab03/Captura%20de%20pantalla%202023-05-29%20225242.png?raw=true">
Ahora hacemos click en ver para ver que el contenido en formato html:

<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/lab03/Captura%20de%20pantalla%202023-05-29%20225257.png?raw=true">
Tambien lo podemos editar haciendo click en el boton del mismo nombre y como vemos nos muestra el texto en markdown nuevamente:

<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/lab03/Captura%20de%20pantalla%202023-05-29%20225305.png?raw=true">
Seguidamente eliminamos dos de los documentos y nos saldrá una venta en la cual nos dice que se eliminó correctamente:

<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/lab03/Captura%20de%20pantalla%202023-05-29%20225329.png?raw=true">

Seguidamente tenemos la lista de documentos actualizada:
<img src="https://github.com/BastleyNait/InformacionIrrelevante/blob/main/lab03/Captura%20de%20pantalla%202023-05-29%20225403.png?raw=true">
#
### II.	SOLUCIÓN DEL CUESTIONARIO

-   **En el Ejemplo "Hola Mundo" con NodeJS. ¿Qué pasó con la línea: "Content type ….."**?
    

No es necesario especificar explícitamente el tipo de contenido en la respuesta utilizando `res.setHeader('Content-type', 'text/html')`. El cliente puede interpretar la respuesta utilizando una plantilla HTML predeterminada. En este caso, el mensaje se mostrará dentro de un elemento `<pre>`. Sin embargo, al utilizar `res.setHeader('Content-type', 'text/html')`, el cliente interpretará que queremos ver la respuesta en un formato HTML específico, por lo que el mensaje se mostrará sin etiquetas dentro del cuerpo del documento.

  

-   **En los ejercicios. ¿En qué lugar debería estar el archivo poema.txt?**
    
El archivo "poema.txt" debería estar ubicado en la carpeta "priv" de acuerdo con la dirección que se pasa a `path.resolve`. Esto significa que se espera que el archivo esté dentro de la carpeta "priv" para que la función `path.resolve` pueda encontrar y acceder a él correctamente. Asegúrate de colocar el archivo "poema.txt" en la ubicación adecuada para que el programa pueda acceder a él correctamente según la ruta especificada.
  

-   **¿Entiende la expresión regular en el código y se da cuenta de para qué es útil?**
    

El código modifica el texto en formato HTML reemplazando los saltos de línea representados por `\n` con la etiqueta `<br>`. Esto se hace para asegurar que el contenido se visualice en el navegador de la misma forma que está en el archivo de texto original, con los saltos de línea correctamente interpretados y mostrados como nuevas líneas en la página. De esta manera, se logra una representación fiel del contenido del archivo de texto en el navegador.  

-   **Note que la respuesta del servidor está en formato JSON, ¿Habrá alguna forma de verla directamente?**  
    


Se puede utilizar `response.send()` para enviar cadenas y arrays directamente sin necesidad de convertirlos a formato JSON. Esto permite que la información se muestre directamente en el cliente sin la necesidad de procesarla como un objeto JSON. Con `response.send()`, los datos se envían tal como están, lo que simplifica el proceso de envío de información y su visualización en el cliente.
## III.	CONCLUSIONES



Durante el desarrollo de este proyecto, se lograron los siguientes objetivos y conclusiones clave:

- Se aprendió a realizar peticiones asíncronas en JavaScript utilizando JSON. Esto permite una comunicación dinámica con servidores o APIs sin recargar la página, lo cual es fundamental para crear aplicaciones web interactivas.

- Se adquirieron conocimientos en programación en el backend utilizando JavaScript. Se exploraron herramientas como Node.js y Express.js, lo que permitió crear servidores web, manejar solicitudes y respuestas, y desarrollar la lógica de negocio en el backend. Esto brinda flexibilidad y eficiencia en el desarrollo de aplicaciones web completas.

- Se comprendió el uso de promesas y objetos no bloqueantes. Las promesas proporcionan una forma estructurada de manejar tareas asíncronas, evitando el anidamiento excesivo de callbacks. Los objetos no bloqueantes permiten que otras tareas se ejecuten sin interrupciones mientras se realizan operaciones asíncronas, mejorando el rendimiento de la aplicación.

En resumen, este proyecto permitió adquirir habilidades importantes en el desarrollo web, como la comunicación asíncrona, la programación en el backend y el manejo de tareas no bloqueantes. Estas habilidades son fundamentales para crear aplicaciones web modernas y eficientes.


<div align="center"><h2> REFERENCIAS Y BIBLIOGRAFÍA </h2></div> 

-   JavaScript code using the latest ECMAScript. Packt Publishing Ltd, 2018.
    
-   Greg Lim. Beginning Node.js, Express & MongoDB Development. Amazon, 2019.
  
-   https://www.w3schools.com/nodejs/nodejs_intro.asp
    
-   https://nodejs.org/en/docs/guides/getting-started-guide/
    
-   https://nodejs.dev/learn
    
-   https://www.w3schools.com/js/js_api_fetch.asp
    
-   https://expressjs.com/es/
    
-   https://developer.mozilla.org/es/docs/Web/API/
