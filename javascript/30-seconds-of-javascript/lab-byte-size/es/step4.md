# Crear un archivo de ejemplo práctico

Ahora creemos un archivo de JavaScript para implementar nuestra función de cálculo de tamaño en bytes de una manera más práctica. Esto demostrará cómo podrías utilizar esta función en una aplicación del mundo real.

1. Crea un nuevo archivo en el WebIDE. Haz clic en el icono de "Nuevo archivo" en la barra lateral del explorador de archivos y asígnalo el nombre `byteSizeCalculator.js`.

2. Añade el siguiente código al archivo:

```javascript
/**
 * Calculate the byte size of a given string.
 * @param {string} str - The string to calculate the byte size for.
 * @returns {number} The size in bytes.
 */
function calculateByteSize(str) {
  return new Blob([str]).size;
}

// Examples with different types of strings
const examples = [
  "Hello World",
  "😀",
  "The quick brown fox jumps over the lazy dog",
  "123!@#$%^&*()",
  "Hello, 世界！",
  "😀😃😄😁"
];

// Display the results
console.log("String Byte Size Calculator\n");
console.log("String".padEnd(45) + "| Characters | Bytes");
console.log("-".repeat(70));

examples.forEach((example) => {
  console.log(
    `"${example}"`.padEnd(45) +
      `| ${example.length}`.padEnd(12) +
      `| ${calculateByteSize(example)}`
  );
});
```

3. Guarda el archivo presionando Ctrl+S o seleccionando Archivo > Guardar desde el menú.

4. Ejecuta el archivo desde la terminal:

```bash
node byteSizeCalculator.js
```

Deberías ver una salida similar a esta:

```
String Byte Size Calculator

String                                      | Characters | Bytes
----------------------------------------------------------------------
"Hello World"                               | 11         | 11
"😀"                                        | 1          | 4
"The quick brown fox jumps over the lazy dog" | 43         | 43
"123!@#$%^&*()"                            | 13         | 13
"Hello, 世界!"                              | 10         | 13
"😀😃😄😁"                                  | 4          | 16
```

Esta tabla muestra claramente la diferencia entre la cantidad de caracteres y el tamaño en bytes para diferentes tipos de cadenas.

Comprender estas diferencias es crucial cuando:

- Estableces límites en la entrada de usuarios en formularios web
- Calculas los requisitos de almacenamiento para datos de texto
- Trabajas con APIs que tienen limitaciones de tamaño
- Optimizas la transferencia de datos a través de redes
