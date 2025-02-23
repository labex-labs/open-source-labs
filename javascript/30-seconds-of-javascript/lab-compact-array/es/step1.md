# Cómo usar Array.prototype.filter() para crear un array compacto

Para crear un array compacto en JavaScript, puedes usar el método `Array.prototype.filter()` para eliminar cualquier valor falsy del array. Los valores falsy incluyen `false`, `null`, `0`, `""`, `undefined` y `NaN`.

A continuación, hay un fragmento de código de ejemplo que demuestra cómo crear un array compacto usando `Array.prototype.filter()`:

```js
const compact = (arr) => arr.filter(Boolean);
```

Luego, puedes usar la función `compact` para crear un array compacto pasando un array como argumento. Por ejemplo:

```js
compact([0, 1, false, 2, "", 3, "a", "e" * 23, NaN, "s", 34]);
// Output: [ 1, 2, 3, 'a','s', 34 ]
```

Al usar `Array.prototype.filter()` de esta manera, puedes crear fácilmente un array compacto que solo contiene valores truthy.
