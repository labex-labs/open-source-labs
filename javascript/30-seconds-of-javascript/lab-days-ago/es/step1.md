# Función de JavaScript para calcular días atrás

Aquí hay una función de JavaScript que calcula la fecha de hace `n` días a partir de hoy y la devuelve como una cadena en el formato `yyyy-mm-dd`:

```js
const daysAgo = (n) => {
  const today = new Date();
  const daysAgoDate = new Date(today.setDate(today.getDate() - Math.abs(n)));
  return daysAgoDate.toISOString().split("T")[0];
};
```

Así es como funciona:

- El constructor `Date` se utiliza para obtener la fecha actual.
- La función `Math.abs()` se utiliza para asegurarse de que el número de días sea positivo.
- La función `Date.prototype.getDate()` se utiliza para obtener el día del mes de la fecha actual.
- La función `Date.prototype.setDate()` se utiliza para actualizar la fecha en consecuencia.
- La fecha resultante se devuelve como una cadena en el formato `yyyy-mm-dd` utilizando la función `Date.prototype.toISOString()`.

Uso de ejemplo:

```js
daysAgo(20); // "2020-09-16" (si la fecha actual es 2020-10-06)
```
