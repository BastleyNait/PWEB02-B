import java.util.Scanner;

public class Main {
    static Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        // Creamos una instancia de la clase Archivos con el objeto testDeIq
        Archivos testDeIq = new Archivos();

        // Leemos el contenido del archivo "TestdeIQ.txt"
        String texto = testDeIq.leerArchivo("TestdeIQ.txt");

        // Dividimos el texto en un arreglo de líneas utilizando el carácter de nueva línea "\n"
        String[] lineas = texto.split("\n");

        // Iteramos sobre el arreglo de cuestionario
        for (int i = 0; i < 20; i++) {
            // Obtenemos la pregunta correspondiente al índice actual
            String pregunta = testDeIq.leerPregunta(lineas, i);

            // Mostramos la pregunta en la consola
            System.out.print(pregunta + "\nRespuesta: ");

            // Leemos la respuesta del usuario desde la consola
            String respuesta = entrada.next();

            // Aquí puedes realizar alguna operación con la respuesta, como compararla con una respuesta esperada

            // Por ejemplo:
            // if (respuesta.equals("respuesta_esperada")) {
            //     // Realizar alguna acción si la respuesta es correcta
            // } else {
            //     // Realizar alguna acción si la respuesta es incorrecta
            // }
        }
    }
}
