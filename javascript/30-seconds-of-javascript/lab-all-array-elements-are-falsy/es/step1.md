# Función para probar si todos los elementos de una matriz son falsy

Para probar si todos los elementos de una matriz son falsy, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.some()` para probar si algún elemento de la colección devuelve `true` en base a la función predicado proporcionada.
3. Si omite el segundo argumento, `fn`, la función usará `Boolean` como predeterminado.
4. La función devuelve `true` si todos los elementos de la matriz son falsy, y `false` en caso contrario.

A continuación, se muestra una implementación de ejemplo de la función:

```js
const none = (arr, fn = Boolean) => !arr.some(fn);
```

Puede usar la función de la siguiente manera:

```js
none([0, 1, 3, 0], (x) => x == 2); // true
none([0, 0, 0]); // true
```
