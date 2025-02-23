# Cómo obtener el día del año en JavaScript utilizando el objeto Date

Para obtener el día del año (número entre 1 y 366) a partir de un objeto `Date` en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el constructor `Date` y `Date.prototype.getFullYear()` para obtener el primer día del año como un objeto `Date`.
3. Reste el primer día del año del objeto `date` y divídalo entre los milisegundos de cada día para obtener el resultado.
4. Utilice `Math.floor()` para redondear el recuento de días resultante a un número entero.

Aquí está el código:

```js
const dayOfYear = (date) =>
  Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
```

Para probar la función, llame a `dayOfYear()` con un objeto `Date` como argumento:

```js
dayOfYear(new Date()); // 272
```
