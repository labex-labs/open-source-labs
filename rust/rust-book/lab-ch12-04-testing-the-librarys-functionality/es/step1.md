# Desarrollo guiado por pruebas

Ahora que hemos extraído la lógica en `src/lib.rs` y hemos dejado la recopilación de argumentos y el manejo de errores en `src/main.rs`, es mucho más fácil escribir pruebas para la funcionalidad central de nuestro código. Podemos llamar directamente a las funciones con varios argumentos y comprobar los valores de retorno sin tener que llamar a nuestro binario desde la línea de comandos.

En esta sección, agregaremos la lógica de búsqueda al programa `minigrep` utilizando el proceso de desarrollo guiado por pruebas (TDD) con los siguientes pasos:

1.  Escribe una prueba que falle y ejecútala para asegurarte de que falle por la razón que esperas.
2.  Escribe o modifica solo el código suficiente para que la nueva prueba pase.
3.  Refactoriza el código que acabas de agregar o cambiar y asegúrate de que las pruebas sigan pasando.
4.  ¡Repite desde el paso 1!

Aunque es solo una de las muchas maneras de escribir software, el TDD puede ayudar a impulsar el diseño del código. Escribir la prueba antes de escribir el código que hace que la prueba pase ayuda a mantener una alta cobertura de pruebas en todo el proceso.

Vamos a probar y desarrollar la implementación de la funcionalidad que realmente buscará la cadena de consulta en el contenido del archivo y producirá una lista de líneas que coincidan con la consulta. Agregaremos esta funcionalidad en una función llamada `search`.
