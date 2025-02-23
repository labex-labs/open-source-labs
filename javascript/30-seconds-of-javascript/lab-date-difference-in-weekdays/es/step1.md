# Contar días hábiles entre dos fechas

Para contar los días hábiles entre dos fechas, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.from()` para crear una matriz con una longitud igual al número de días entre `startDate` y `endDate`.
3. Utilice `Array.prototype.reduce()` para iterar sobre la matriz, comprobando si cada fecha es un día hábil e incrementando `count`.
4. Actualice `startDate` con el día siguiente en cada bucle utilizando `Date.prototype.getDate()` y `Date.prototype.setDate()` para avanzarla un día.
5. Tenga en cuenta que esta función no tiene en cuenta los días festivos oficiales.

Aquí está el código para implementar esto:

```js
const countWeekDaysBetween = (startDate, endDate) =>
  Array.from({ length: (endDate - startDate) / (1000 * 3600 * 24) }).reduce(
    (count) => {
      if (startDate.getDay() % 6 !== 0) count++;
      startDate = new Date(startDate.setDate(startDate.getDate() + 1));
      return count;
    },
    0
  );
```

Puede utilizar el siguiente código para probar la función:

```js
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 06, 2020")); // 1
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 14, 2020")); // 7
```
