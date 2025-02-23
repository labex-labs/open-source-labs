# Función para Devolver la Última Fecha de un Mes

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

Esta función devuelve la última fecha del mes para la fecha dada.

Para lograr esto, sigue estos pasos:

1. Utiliza `Date.prototype.getFullYear()` y `Date.prototype.getMonth()` para obtener el año y el mes actuales a partir de la fecha dada.
2. Crea una nueva fecha con el año y el mes dados incrementados en `1`, y el día establecido en `0` (último día del mes anterior). Puedes utilizar el constructor `Date` para este propósito.
3. Si no se le pasa ningún argumento a la función, utilizará la fecha actual por defecto.
4. Devuelve la última fecha del mes en el formato de una representación de cadena de la fecha.

Aquí está el código de la función:

```js
const getLastDateOfMonth = (date = new Date()) => {
  let lastDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
  return lastDate.toISOString().split("T")[0];
};
```

Puedes probar la función llamándola con un objeto de fecha como este:

```js
getLastDateOfMonth(new Date("2015-08-11")); // '2015-08-30'
```
