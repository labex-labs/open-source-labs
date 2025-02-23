# Función de JavaScript para Calcular la Diferencia de Fechas en Horas

Para calcular la diferencia entre dos fechas en horas utilizando JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

2. Utilice la siguiente función de JavaScript para obtener la diferencia (en horas) entre dos objetos `Date`:

```js
const getHoursDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600);
```

3. Llame a la función con las dos fechas como argumentos para obtener la diferencia en horas:

```js
getHoursDiffBetweenDates(
  new Date("2021-04-24 10:25:00"),
  new Date("2021-04-25 10:25:00")
); // 24
```
