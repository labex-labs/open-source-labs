# Práctica de código: Obtener elementos aleatorios de una matriz

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. El siguiente código utiliza el algoritmo de Fisher-Yates para barajar una matriz y recuperar `n` elementos aleatorios y únicos en claves únicas de la matriz, hasta el tamaño de la matriz.

```js
const sampleSize = ([...arr], n = 1) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr.slice(0, n);
};
```

Para utilizar este código, llama a `sampleSize()` con una matriz y un número opcional `n` de elementos a recuperar. Si no se proporciona `n`, la función devolverá solo un elemento al azar de la matriz.

```js
sampleSize([1, 2, 3], 2); // [3, 1]
sampleSize([1, 2, 3], 4); // [2, 3, 1]
```
