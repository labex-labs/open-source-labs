# Dividir en trozos una iterable

Para dividir una iterable en arrays más pequeños de un tamaño especificado, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza un bucle `for...of` sobre la iterable dada, utilizando `Array.prototype.push()` para agregar cada nuevo valor al `chunk` actual.
3. Verifica si el `chunk` actual es del tamaño deseado utilizando `Array.prototype.length` y devuelve el valor si es así.
4. Verifica el último `chunk` utilizando `Array.prototype.length` y devuélvelo si no está vacío.
5. Utiliza el siguiente código:

```js
const chunkify = function* (itr, size) {
  let chunk = [];
  for (const v of itr) {
    chunk.push(v);
    if (chunk.length === size) {
      yield chunk;
      chunk = [];
    }
  }
  if (chunk.length) yield chunk;
};
```

6. Utiliza este código para probar la función:

```js
const x = new Set([1, 2, 1, 3, 4, 1, 2, 5]);
[...chunkify(x, 2)]; // [[1, 2], [3, 4], [5]]
```
