# Entendiendo los cálculos de fechas en JavaScript

Ahora que entendemos cómo crear objetos `Date`, aprendamos cómo calcular la diferencia entre dos fechas.

## Aritmética de fechas en JavaScript

JavaScript te permite realizar operaciones aritméticas directamente en objetos `Date`. Cuando restas un objeto `Date` de otro, JavaScript automáticamente los convierte en marcas de tiempo (milisegundos) y realiza la resta.

```javascript
let date1 = new Date("2023-01-01T00:00:00");
let date2 = new Date("2023-01-01T00:01:00");

let differenceInMilliseconds = date2 - date1;
console.log(differenceInMilliseconds); // 60000 (60 segundos * 1000 milisegundos)
```

Intenta ejecutar este código en tu entorno de Node.js. El resultado debería ser `60000`, que representa 60 segundos en milisegundos.

## Convirtiendo milisegundos a segundos

Para convertir una diferencia de tiempo de milisegundos a segundos, simplemente dividimos entre 1000:

```javascript
let differenceInSeconds = differenceInMilliseconds / 1000;
console.log(differenceInSeconds); // 60
```

Esto nos da la diferencia de tiempo en segundos, que en este ejemplo es 60 segundos o 1 minuto.

## Creando una función para calcular la diferencia de fechas

Ahora que entendemos el concepto, creemos una función simple para calcular la diferencia entre dos fechas en segundos:

```javascript
function getDateDifferenceInSeconds(startDate, endDate) {
  return (endDate - startDate) / 1000;
}

// Prueba la función
let start = new Date("2023-01-01T00:00:00");
let end = new Date("2023-01-01T00:01:30");
let difference = getDateDifferenceInSeconds(start, end);
console.log(difference); // 90 (1 minuto y 30 segundos)
```

Intenta escribir y ejecutar esta función en el entorno de Node.js. El resultado debería ser `90`, que representa 1 minuto y 30 segundos.
