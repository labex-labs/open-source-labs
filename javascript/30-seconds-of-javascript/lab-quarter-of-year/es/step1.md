# Función para Determinar el Trimestre del Año

Para determinar el trimestre del año, utiliza la función `quarterOfYear()`. Esta función toma un argumento `date` opcional y devuelve un array con el trimestre y el año al que pertenece la fecha suministrada.

Para utilizar esta función, abre la Terminal/SSH y escribe `node`. Luego, copia y pega el siguiente código:

```js
const quarterOfYear = (date = new Date()) => [
  Math.ceil((date.getMonth() + 1) / 3),
  date.getFullYear()
];
```

La función `quarterOfYear()` utiliza los siguientes pasos para calcular el trimestre y el año:

- Utiliza `Date.prototype.getMonth()` para obtener el mes actual en el rango (0, 11), suma `1` para mapearlo al rango (1, 12).
- Utiliza `Math.ceil()` y divide el mes por `3` para obtener el trimestre actual.
- Utiliza `Date.prototype.getFullYear()` para obtener el año a partir de la `date` dada.
- Omite el argumento `date` para utilizar la fecha actual por defecto.

A continuación, se presentan algunos ejemplos de cómo utilizar la función `quarterOfYear()`:

```js
quarterOfYear(new Date("07/10/2018")); // [ 3, 2018 ]
quarterOfYear(); // [ 4, 2020 ]
```
