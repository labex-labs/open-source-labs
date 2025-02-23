# Función para agregar días hábiles a una fecha dada

Para calcular una fecha futura sumando un número dado de días hábiles, puedes utilizar la función `addWeekDays`. Aquí están los pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la función `addWeekDays` que toma dos argumentos: `startDate` y `count`.
3. `startDate` es la fecha a partir de la cual desea comenzar a agregar días hábiles.
4. `count` es el número de días hábiles que desea agregar a la fecha de inicio.
5. La función construye un array utilizando el método `Array.from()` y establece la longitud igual al `count` de días hábiles a agregar.
6. El método `Array.prototype.reduce()` se utiliza para iterar sobre el array, comenzando desde `startDate`, e incrementarlo utilizando `Date.prototype.getDate()` y `Date.prototype.setDate()`.
7. La función verifica si la `date` actual es un fin de semana o no.
8. Si la `date` actual es un fin de semana, la función la actualiza nuevamente sumando uno o dos días para que sea un día hábil.
9. La función no tiene en cuenta los días feriados oficiales.

```js
const addWeekDays = (startDate, count) =>
  Array.from({ length: count }).reduce((date) => {
    date = new Date(date.setDate(date.getDate() + 1));
    if (date.getDay() % 6 === 0)
      date = new Date(date.setDate(date.getDate() + (date.getDay() / 6 + 1)));
    return date;
  }, startDate);
```

Aquí hay algunos ejemplos de cómo puedes utilizar la función `addWeekDays`:

```js
addWeekDays(new Date("Oct 09, 2020"), 5); // 'Oct 16, 2020'
addWeekDays(new Date("Oct 12, 2020"), 5); // 'Oct 19, 2020'
```
