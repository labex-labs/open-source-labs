# Obtener la fecha de mañana

Para practicar la codificación, puedes comenzar abriendo la Terminal/SSH y escribiendo `node`. Una vez que hayas hecho esto, puedes obtener la fecha de mañana con los siguientes pasos:

1. Utiliza el constructor `Date` para obtener la fecha actual.
2. Incrementa la fecha en uno utilizando `Date.prototype.getDate()`.
3. Establece el valor al resultado utilizando `Date.prototype.setDate()`.
4. Utiliza `Date.prototype.toISOString()` para devolver una cadena en el formato `yyyy-mm-dd`.

Aquí está el código que puedes utilizar:

```js
const tomorrow = () => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + 1);
  return currentDate.toISOString().split("T")[0];
};
```

Una vez que hayas ingresado este código, puedes obtener la fecha de mañana llamando a la función `tomorrow()`. Por ejemplo, si la fecha de hoy es 2018-10-18, la salida será `2018-10-19`.
