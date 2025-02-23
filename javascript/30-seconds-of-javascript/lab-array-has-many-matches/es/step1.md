# Función para comprobar si una matriz tiene múltiples coincidencias

Para comprobar si una matriz tiene más de un valor que coincide con una función dada, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.filter()` en combinación con `fn` para encontrar todos los elementos de matriz que coinciden.
3. Utilice `Array.prototype.length` para comprobar si más de un elemento coincide con `fn`.

Aquí está el código que puede utilizar:

```js
const hasMany = (arr, fn) => arr.filter(fn).length > 1;
```

Y aquí hay algunos ejemplos:

```js
hasMany([1, 3], (x) => x % 2); // true
hasMany([1, 2], (x) => x % 2); // false
```
