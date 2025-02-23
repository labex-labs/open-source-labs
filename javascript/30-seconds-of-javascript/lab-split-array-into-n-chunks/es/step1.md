# Cómo dividir un array en N trozos

Para dividir un array en `n` arrays más pequeños, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Math.ceil()` y `Array.prototype.length` para calcular el tamaño de cada trozo.
3. Utiliza `Array.from()` para crear un nuevo array de tamaño `n`.
4. Utiliza `Array.prototype.slice()` para mapear cada elemento del nuevo array a un trozo de longitud `size`.
5. Si el array original no se puede dividir uniformemente, el último trozo contendrá los elementos restantes.

A continuación, se muestra una implementación de ejemplo de la función `chunkIntoN` en JavaScript:

```js
const chunkIntoN = (arr, n) => {
  const size = Math.ceil(arr.length / n);
  return Array.from({ length: n }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
};
```

Puedes utilizar esta función para dividir un array en `n` trozos pasando el array y el número deseado de trozos como argumentos. Por ejemplo:

```js
chunkIntoN([1, 2, 3, 4, 5, 6, 7], 4); // [[1, 2], [3, 4], [5, 6], [7]]
```
