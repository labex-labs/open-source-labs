# Crear una función para validar cadenas de fechas en formato ISO

En este paso, crearemos una función de JavaScript que verifique si una cadena dada está en un formato ISO 8601 válido.

## Crear la función de validación

Creemos un nuevo archivo de JavaScript para nuestro validador de fechas ISO:

1. En el WebIDE, haz clic en el icono del Explorador en la barra lateral izquierda.
2. Haz clic derecho en el explorador de archivos y selecciona "Nuevo archivo".
3. Nombrar el archivo `isISODate.js` y presionar Enter.
4. Agrega el siguiente código al archivo:

```javascript
/**
 * Checks if a string is a valid ISO 8601 formatted date string
 * @param {string} val - The string to check
 * @return {boolean} - Returns true if the string is in ISO format, false otherwise
 */
const isISOString = (val) => {
  // Create a Date object from the input string
  const d = new Date(val);

  // Check if the date is valid (not NaN) and if the ISO string matches the original
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

// Export the function so we can use it elsewhere
module.exports = isISOString;
```

Examinemos cómo funciona esta función:

1. `new Date(val)` crea un objeto Date a partir de la cadena de entrada.
2. `d.valueOf()` devuelve el valor numérico de la marca de tiempo (milisegundos desde el 1 de enero de 1970).
3. `Number.isNaN(d.valueOf())` verifica si la fecha es inválida (NaN significa "No es un número").
4. `d.toISOString() === val` verifica que convertir la fecha de nuevo a una cadena ISO coincida con la entrada original.

## Probar nuestra función

Ahora, creemos un archivo de prueba simple para probar nuestra función:

1. Crea otro archivo llamado `testISO.js`.
2. Agrega el siguiente código:

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Test with a valid ISO formatted date
console.log("Testing a valid ISO date:");
console.log("2020-10-12T10:10:10.000Z");
console.log("Result:", isISOString("2020-10-12T10:10:10.000Z"));
console.log();

// Test with an invalid format
console.log("Testing a non-ISO date:");
console.log("2020-10-12");
console.log("Result:", isISOString("2020-10-12"));
```

3. Ejecuta el archivo de prueba utilizando Node.js:

```bash
node testISO.js
```

Deberías ver una salida similar a:

```
Testing a valid ISO date:
2020-10-12T10:10:10.000Z
Result: true

Testing a non-ISO date:
2020-10-12
Result: false
```

Esto muestra que nuestra función identifica correctamente que "2020-10-12T10:10:10.000Z" es una fecha en formato ISO válida, mientras que "2020-10-12" no lo es.
