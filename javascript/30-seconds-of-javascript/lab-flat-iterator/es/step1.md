# Explicación del iterador plano

Para crear un generador que itere sobre un iterable y aplane los iterables anidados, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la recursividad en la función generadora.
3. Utilice un bucle `for...of` para iterar sobre los valores del iterable dado.
4. Utilice `Symbol.iterator` para comprobar si cada valor es un iterable.
5. Si es así, utilice la expresión `yield*` para delegar recursivamente a la misma función generadora.
6. De lo contrario, `yield` el valor actual.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const flatIterator = function* (itr) {
  for (let item of itr) {
    if (item[Symbol.iterator]) yield* flatIterator(item);
    else yield item;
  }
};

const arr = [1, 2, [3, 4], [5, [6, [7], 8]], 9, new Set([10, 11])];
[...flatIterator(arr)]; // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
```

En el ejemplo, `arr` es un array de valores, que incluye arrays anidados y un conjunto. La función generadora `flatIterator` se utiliza para aplanar estos valores anidados y devolver un array aplanado.
