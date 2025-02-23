# Cómo obtener la marca de tiempo Unix a partir de una fecha en JavaScript

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

Puedes utilizar los siguientes pasos para obtener la marca de tiempo Unix a partir de un objeto `Date` en JavaScript:

1. Utiliza `Date.prototype.getTime()` para obtener la marca de tiempo en milisegundos.
2. Divide la marca de tiempo entre `1000` para obtener la marca de tiempo en segundos.
3. Utiliza `Math.floor()` para redondear la marca de tiempo resultante a un entero.
4. Si omites el argumento `date`, se utilizará la fecha actual.

Aquí hay un fragmento de código de ejemplo:

```js
const getTimestamp = (date = new Date()) => Math.floor(date.getTime() / 1000);
```

Puedes llamar a la función `getTimestamp()` para obtener la marca de tiempo Unix. Por ejemplo:

```js
getTimestamp(); // 1602162242
```
