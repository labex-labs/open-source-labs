# Función para comprobar si una matriz tiene solo una coincidencia

Para comprobar si una matriz tiene solo un valor que coincide con la función dada, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.filter()` en combinación con `fn` para encontrar todos los elementos de matriz que coinciden.
3. Utilice `Array.prototype.length` para comprobar si solo un elemento coincide con `fn`.

Aquí está el código:

```js
const hasOne = (arr, fn) => arr.filter(fn).length === 1;
```

Y aquí está un ejemplo:

```js
hasOne([1, 2], (x) => x % 2); // true
hasOne([1, 3], (x) => x % 2); // false
```
