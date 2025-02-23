# Función para calcular la diferencia de fechas en días

Para calcular la diferencia entre dos fechas en días, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la función `getDaysDiffBetweenDates` con dos objetos `Date` como argumentos.
3. La función restará la fecha inicial de la fecha final y dividirá el resultado entre el número de milisegundos en un día para obtener la diferencia en días entre ellas.

Aquí está el código de la función `getDaysDiffBetweenDates`:

```js
const getDaysDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600 * 24);
```

Para utilizar la función, pase dos objetos `Date` en el formato `YYYY-MM-DD`:

```js
getDaysDiffBetweenDates(new Date("2017-12-13"), new Date("2017-12-22")); // 9
```

Esto devolverá la diferencia entre las dos fechas en días, que es 9 en este ejemplo.
