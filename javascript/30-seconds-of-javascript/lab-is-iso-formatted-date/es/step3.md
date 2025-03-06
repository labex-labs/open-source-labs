# Pruebas con diversos formatos de fecha

Ahora que tenemos nuestra función de validación básica, probémosla con diferentes formatos de fecha para entender cómo se comporta con diversas entradas.

## Crear un conjunto de pruebas

Creemos un conjunto de pruebas completo para examinar diferentes formatos de fecha:

1. Crea un nuevo archivo llamado `dateTester.js`.
2. Agrega el siguiente código:

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Function to test different date strings
function testDate(description, dateString) {
  console.log(`Testing: ${description}`);
  console.log(`Input: "${dateString}"`);
  console.log(`Is ISO Format: ${isISOString(dateString)}`);
  console.log("-----------------------");
}

// Valid ISO date examples
testDate("Standard ISO date with timezone Z", "2023-05-12T14:30:15.123Z");
testDate("ISO date with zero milliseconds", "2020-10-12T10:10:10.000Z");

// Invalid or non-ISO format examples
testDate("Date only (no time component)", "2023-05-12");
testDate("Date and time without milliseconds", "2023-05-12T14:30:15Z");
testDate(
  "Date with time zone offset instead of Z",
  "2023-05-12T14:30:15+01:00"
);
testDate("Invalid date (month 13 does not exist)", "2023-13-12T14:30:15.123Z");
testDate("Non-date string", "Hello World");
```

3. Ejecuta el conjunto de pruebas en la terminal:

```bash
node dateTester.js
```

Deberías ver una salida que muestre qué cadenas son fechas ISO válidas y cuáles no.

## Comprender los resultados

Analicemos qué hace que cada caso de prueba sea válido o inválido:

1. `2023-05-12T14:30:15.123Z` - Esto es válido porque sigue el formato ISO 8601 completo con el indicador de zona horaria UTC (Z).

2. `2020-10-12T10:10:10.000Z` - Esto también es válido, con los milisegundos establecidos explícitamente en 000.

3. `2023-05-12` - Esta es una fecha válida, pero no está en formato ISO porque le falta la componente de tiempo.

4. `2023-05-12T14:30:15Z` - Esto parece ser un formato ISO, pero le faltan los milisegundos, que son obligatorios en el formato ISO estricto.

5. `2023-05-12T14:30:15+01:00` - Esto utiliza un desplazamiento de zona horaria (+01:00) en lugar de 'Z'. Si bien esto es válido según ISO 8601, nuestra función requiere el formato exacto producido por `toISOString()`, que siempre utiliza 'Z'.

6. `2023-13-12T14:30:15.123Z` - Esta es una fecha inválida (el mes 13 no existe), por lo que `new Date()` creará un objeto Date inválido.

7. `Hello World` - Esto no es una fecha en absoluto, por lo que `new Date()` creará un objeto Date inválido.

Nuestra función de validación comprueba específicamente dos condiciones:

1. La cadena debe convertirse en una fecha válida (no NaN).
2. Cuando esa fecha se convierte de nuevo en una cadena ISO, debe coincidir exactamente con la entrada original.

Este enfoque asegura que estamos validando el formato ISO exacto producido por el método `toISOString()` de JavaScript.
