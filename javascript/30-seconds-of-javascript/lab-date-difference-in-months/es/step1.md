# Función para Calcular la Diferencia de Fechas en Meses

Para calcular la diferencia entre dos fechas en meses, utiliza la siguiente función:

```js
const getMonthsDiffBetweenDates = (dateInitial, dateFinal) =>
  Math.max(
    (dateFinal.getFullYear() - dateInitial.getFullYear()) * 12 +
      dateFinal.getMonth() -
      dateInitial.getMonth(),
    0
  );
```

Para usar esta función, pasa dos objetos `Date` como argumentos. Por ejemplo:

```js
getMonthsDiffBetweenDates(new Date("2017-12-13"), new Date("2018-04-29")); // 4
```

Esta función utiliza los métodos `Date.prototype.getFullYear()` y `Date.prototype.getMonth()` para calcular la diferencia en meses entre dos fechas.
