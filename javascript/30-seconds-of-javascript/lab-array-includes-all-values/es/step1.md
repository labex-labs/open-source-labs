# Función para comprobar si una matriz incluye todos los valores

Si desea comprobar si todos los elementos de una matriz `values` están incluidos en otra matriz `arr`, puede usar la función `includesAll` en JavaScript.

Para comenzar a usar la función, abra la Terminal/SSH y escriba `node`.

Aquí está cómo funciona la función `includesAll`:

- Utiliza los métodos `Array.prototype.every()` y `Array.prototype.includes()` para comprobar si todos los elementos de `values` están incluidos en `arr`.
- Si todos los elementos de `values` están incluidos en `arr`, la función devolverá `true`. De lo contrario, devolverá `false`.

```js
const includesAll = (arr, values) => values.every((v) => arr.includes(v));
```

Aquí hay un ejemplo de cómo usar la función `includesAll`:

```js
includesAll([1, 2, 3, 4], [1, 4]); // true
includesAll([1, 2, 3, 4], [1, 5]); // false
```
