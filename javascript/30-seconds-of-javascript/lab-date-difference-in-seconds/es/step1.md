# Función para Calcular la Diferencia de Fechas en Segundos

Para calcular la diferencia entre dos fechas en segundos, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Resta los dos objetos `Date` y divide por el número de milisegundos en un segundo.
3. El resultado será la diferencia entre las dos fechas en segundos.

Aquí está una función de JavaScript que realiza este cálculo:

```js
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

Para usar esta función, pasa dos objetos `Date` como argumentos, así:

```js
getSecondsDiffBetweenDates(
  new Date("2020-12-24 00:00:15"),
  new Date("2020-12-24 00:00:17")
); // 2
```
