# Comprobar si una Fecha está entre dos Fechas

Para comprobar si una fecha está entre dos fechas otras, utiliza los operadores mayor que (`>`) y menor que (`<`) en JavaScript. Aquí hay una función de ejemplo:

```js
const isBetweenDates = (dateStart, dateEnd, date) =>
  date > dateStart && date < dateEnd;
```

Para utilizar esta función, pasa la fecha de inicio, la fecha de finalización y la fecha a comprobar. La función devolverá `true` si la fecha está entre la fecha de inicio y la fecha de finalización, y `false` en caso contrario. Aquí hay algunos ejemplos:

```js
isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 19)
); // false

isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 25)
); // true
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
