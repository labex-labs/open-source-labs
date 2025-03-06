# Implementando la función de diferencia de fechas utilizando funciones flecha

Ahora que entendemos cómo calcular diferencias de fechas, implementemos una versión más concisa de nuestra función utilizando funciones flecha.

## Funciones flecha en JavaScript

Las funciones flecha proporcionan una sintaxis más corta para escribir funciones en JavaScript. Así es como podemos reescribir nuestra función de diferencia de fechas utilizando la sintaxis de función flecha:

```javascript
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

Esta función hace exactamente lo mismo que nuestra función anterior, pero con una sintaxis más limpia y concisa.

## Creando un archivo JavaScript

Creemos un archivo JavaScript para almacenar y probar nuestra función. Salga del entorno de Node.js presionando Ctrl+D o escribiendo `.exit` y presionando Enter.

Ahora, cree un nuevo archivo llamado `dateDifference.js` en el WebIDE:

1. Haga clic en el icono "Explorer" en la barra lateral izquierda.
2. Haga clic derecho en el explorador de archivos y seleccione "New File".
3. Nombre el archivo `dateDifference.js` y presione Enter.
4. Agregue el siguiente código al archivo:

```javascript
// Función para calcular la diferencia entre dos fechas en segundos
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Ejemplos de prueba
console.log("Example 1:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:15"),
    new Date("2020-12-24 00:00:17")
  )
); // Salida esperada: 2

console.log("\nExample 2:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 00:01:00")
  )
); // Salida esperada: 60

console.log("\nExample 3:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 01:00:00")
  )
); // Salida esperada: 3600
```

Guarde el archivo presionando Ctrl+S o haciendo clic en Archivo > Guardar.

## Ejecutando el archivo JavaScript

Para ejecutar el archivo que acabamos de crear, use el siguiente comando en la terminal:

```bash
node dateDifference.js
```

Debería ver la siguiente salida:

```
Example 1:
2

Example 2:
60

Example 3:
3600
```

Esto confirma que nuestra función está funcionando correctamente:

- Primer ejemplo: La diferencia entre 00:00:15 y 00:00:17 es de 2 segundos.
- Segundo ejemplo: La diferencia entre 00:00:00 y 00:01:00 es de 60 segundos (1 minuto).
- Tercer ejemplo: La diferencia entre 00:00:00 y 01:00:00 es de 3600 segundos (1 hora).
