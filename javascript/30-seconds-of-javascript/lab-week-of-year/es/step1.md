# Obtener la semana del año a partir de una fecha en JavaScript

Para obtener la semana del año con índice cero que corresponde a una fecha en JavaScript, siga estos pasos:

1. Cree una función `weekOfYear` que tome un parámetro `date`.
2. Utilice el constructor `Date` y `Date.prototype.getFullYear()` para obtener el primer día del año como un objeto `Date`.
3. Utilice `Date.prototype.setDate()`, `Date.prototype.getDate()` y `Date.prototype.getDay()` junto con el operador módulo (`%`) para obtener el primer lunes del año.
4. Reste el primer lunes del año de la fecha (`date`) dada y divida por el número de milisegundos en una semana.
5. Utilice `Math.round()` para obtener la semana del año con índice cero correspondiente a la fecha (`date`) dada.
6. Si la fecha (`date`) dada es anterior al primer lunes del año, se devuelve `-0`.

Aquí está el código:

```js
const weekOfYear = (date) => {
  const startOfYear = new Date(date.getFullYear(), 0, 1);
  startOfYear.setDate(startOfYear.getDate() + (startOfYear.getDay() % 7));
  return Math.round((date - startOfYear) / (7 * 24 * 3600 * 1000));
};
```

Para utilizar la función `weekOfYear`, simplemente llámela con un objeto `Date` como parámetro:

```js
weekOfYear(new Date("2021-06-18")); // 23
```

Esto devolverá la semana del año con índice cero que corresponde a la fecha dada, que en este caso es `23`.
