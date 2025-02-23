# Función para calcular la diferencia de fechas en minutos

Para calcular la diferencia (en minutos) entre dos fechas, utiliza la siguiente función:

```js
const getMinutesDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 60);
```

Simplemente resta los dos objetos `Date` y divídelo por el número de milisegundos en un minuto para obtener la diferencia (en minutos) entre ellos.

Aquí hay un ejemplo de uso de la función:

```js
getMinutesDiffBetweenDates(
  new Date("2021-04-24 01:00:15"),
  new Date("2021-04-24 02:00:15")
); // 60
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
