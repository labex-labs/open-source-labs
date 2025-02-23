# Generador de rangos de fechas

Para generar todas las fechas en un rango dado con un paso dado, utiliza el siguiente código en Terminal/SSH y escribe `node`:

```js
const dateRangeGenerator = function* (start, end, step = 1) {
  let d = start;
  while (d < end) {
    yield new Date(d);
    d.setDate(d.getDate() + step);
  }
};
```

Esto crea un generador que utiliza un bucle `while` para iterar desde `start` hasta `end`, utilizando el constructor `Date` para devolver cada fecha en el rango e incrementando en `step` días utilizando `Date.prototype.getDate()` y `Date.prototype.setDate()`.

Para utilizar un valor predeterminado de `1` para `step`, omite el tercer argumento.

Aquí hay un ejemplo de cómo utilizar el `dateRangeGenerator`:

```js
[...dateRangeGenerator(new Date("2021-06-01"), new Date("2021-06-04"))];
// [ 2021-06-01, 2021-06-02, 2021-06-03 ]
```
