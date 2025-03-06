# Empezando con los objetos Date de JavaScript

JavaScript proporciona un objeto `Date` incorporado que nos permite trabajar con fechas y horas. Antes de calcular la diferencia entre fechas, primero entendamos cómo crear y trabajar con objetos `Date` en JavaScript.

## Iniciando el entorno de Node.js

Comencemos abriendo el entorno interactivo de Node.js:

1. Abra la Terminal haciendo clic en el menú Terminal en la parte superior del WebIDE.
2. Escriba el siguiente comando y presione Enter:

```bash
node
```

Ahora debería ver el indicador de Node.js (`>`), lo que indica que está en el entorno interactivo de JavaScript. Esto le permite ejecutar código JavaScript directamente en la terminal.

![node-prompt](../assets/screenshot-20250306-328ScUbO@2x.png)

## Creando objetos Date

En JavaScript, podemos crear un nuevo objeto `Date` de varias maneras:

```javascript
// Fecha y hora actuales
let now = new Date();
console.log(now);

// Fecha y hora específicas (año, mes [0-11], día, hora, minuto, segundo)
let specificDate = new Date(2023, 0, 15, 10, 30, 45); // 15 de enero de 2023, 10:30:45
console.log(specificDate);

// Fecha a partir de una cadena
let dateFromString = new Date("2023-01-15T10:30:45");
console.log(dateFromString);
```

Intente escribir cada uno de estos ejemplos en el entorno de Node.js y observe la salida.

Tenga en cuenta que en JavaScript, los meses se indexan a partir de cero, lo que significa que enero es 0, febrero es 1, y así sucesivamente.

## Obteniendo la marca de tiempo (timestamp) de los objetos Date

Cada objeto `Date` en JavaScript almacena internamente la hora como el número de milisegundos que han pasado desde el 1 de enero de 1970 (UTC). Esto se conoce como una marca de tiempo (timestamp).

```javascript
let now = new Date();
console.log(now.getTime()); // Obtener la marca de tiempo en milisegundos
```

Esta marca de tiempo será útil para calcular la diferencia entre fechas.
