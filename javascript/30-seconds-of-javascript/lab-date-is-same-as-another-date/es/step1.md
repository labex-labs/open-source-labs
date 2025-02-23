# Comprobar si dos fechas son iguales

Para comprobar si dos fechas son iguales, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Date.prototype.toISOString()` y la comprobación de igualdad estricta (`===`) para comparar las dos fechas.
3. Aquí hay un fragmento de código de ejemplo:

```js
const isSameDate = (dateA, dateB) =>
  dateA.toISOString() === dateB.toISOString();
```

4. Pruebe la función con dos fechas como argumentos para ver si son iguales:

```js
isSameDate(new Date(2010, 10, 20), new Date(2010, 10, 20)); // true
```

Esta función comprueba si las dos fechas son iguales al comparar sus representaciones de cadena ISO.
