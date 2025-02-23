# Cómo encontrar la similitud de arrays en JavaScript

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Esto te ayudará a entender cómo encontrar un array de elementos que aparecen en ambos arrays. Sigue estos pasos:

1. Utiliza el método `Array.prototype.includes()` para determinar los valores que no son parte de `values`.
2. Utiliza el método `Array.prototype.filter()` para eliminarlos.

Aquí está el código para encontrar la similitud de arrays:

```js
const similarity = (arr, values) => arr.filter((v) => values.includes(v));
```

Puedes probar este código ejecutando el siguiente comando:

```js
similarity([1, 2, 3], [1, 2, 4]); // [1, 2]
```

Esto devolverá `[1, 2]` como salida.
