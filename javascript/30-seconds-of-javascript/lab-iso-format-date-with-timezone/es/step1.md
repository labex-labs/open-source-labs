# Convertir fechas al formato ISO con zona horaria

Para convertir una fecha al formato ISO extendido (ISO 8601), incluyendo el desplazamiento de zona horaria, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a codificar.
2. Utilice `Date.prototype.getTimezoneOffset()` para obtener el desplazamiento de zona horaria y revertirlo. Guarde su signo en `diff`.
3. Defina una función auxiliar, `pad()`, que normalice cualquier número pasado a un entero usando `Math.floor()` y `Math.abs()` y lo rellene a `2` dígitos, usando `String.prototype.padStart()`.
4. Utilice `pad()` y los métodos integrados en el prototipo `Date` para construir la cadena ISO 8601 con desplazamiento de zona horaria.

Aquí está el código que puede utilizar:

```js
const toISOStringWithTimezone = (date) => {
  const tzOffset = -date.getTimezoneOffset();
  const diff = tzOffset >= 0 ? "+" : "-";
  const pad = (n) => `${Math.floor(Math.abs(n))}`.padStart(2, "0");
  return (
    date.getFullYear() +
    "-" +
    pad(date.getMonth() + 1) +
    "-" +
    pad(date.getDate()) +
    "T" +
    pad(date.getHours()) +
    ":" +
    pad(date.getMinutes()) +
    ":" +
    pad(date.getSeconds()) +
    diff +
    pad(tzOffset / 60) +
    ":" +
    pad(tzOffset % 60)
  );
};
```

Utilice la función `toISOStringWithTimezone()` con un objeto `new Date()` como argumento para obtener la fecha en formato ISO con desplazamiento de zona horaria. Por ejemplo:

```js
toISOStringWithTimezone(new Date()); // '2020-10-06T20:43:33-04:00'
```
