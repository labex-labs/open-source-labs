# Encontrando la Fecha Máxima

Para encontrar el valor máximo de fecha de una matriz dada de fechas, siga estos pasos:

1. Abra la Terminal o SSH.
2. Escriba `node` para comenzar a practicar la codificación.
3. Utilice la sintaxis de propagación ES6 con `Math.max()` para encontrar el valor máximo de fecha.
4. Convierta el valor máximo de fecha en un objeto `Date` utilizando el constructor `Date`.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const maxDate = (...dates) => new Date(Math.max(...dates));

const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];

maxDate(...dates); // Devuelve "2018-03-11T22:00:00.000Z"
```

Siguiendo estos pasos y utilizando el código proporcionado, puede encontrar fácilmente el valor máximo de fecha de una matriz dada de fechas.
