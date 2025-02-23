# Función para calcular la fecha de 'n' días a partir de hoy

Para calcular la fecha de 'n' días a partir de hoy, siga estos pasos:

- Abra la Terminal/SSH y escriba 'node' para comenzar a practicar la codificación.
- Utilice el constructor `Date` para obtener la fecha actual.
- Utilice `Math.abs()` y `Date.prototype.getDate()` para actualizar la fecha en consecuencia.
- Establezca el resultado utilizando `Date.prototype.setDate()`.
- Utilice `Date.prototype.toISOString()` para devolver una cadena en el formato `yyyy-mm-dd`.

Aquí está el código:

```js
const daysFromNow = (n) => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + Math.abs(n));
  return currentDate.toISOString().split("T")[0];
};
```

Uso de ejemplo:

```js
daysFromNow(5); // Salida: 2020-10-13 (si la fecha actual es 2020-10-08)
```
