# Comprobar si una fecha es un día de la semana

Para comprobar si una fecha determinada es un día de la semana, puedes utilizar el siguiente fragmento de código:

```js
const isWeekday = (date = new Date()) => date.getDay() % 6 !== 0;
```

- Esta función utiliza `Date.prototype.getDay()` para obtener el día de la semana como un número (0-6), donde el domingo es 0 y el sábado es 6.
- Luego comprueba si el día de la semana no es igual a 0 (domingo) o 6 (sábado), lo que significa que es un día de la semana.
- Si no se proporciona una fecha como argumento, se utiliza la fecha actual como predeterminada.

Uso de ejemplo:

```js
isWeekday(); // true (si la fecha actual es un día de la semana)
isWeekday(new Date(2021, 5, 28)); // true (si la fecha es un día de la semana)
```
