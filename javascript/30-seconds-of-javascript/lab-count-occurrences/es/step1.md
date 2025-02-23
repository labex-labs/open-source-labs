# Cómo contar ocurrencias en JavaScript

Para contar el número de veces que aparece un valor específico en una matriz (array) de JavaScript, puedes utilizar el método `Array.prototype.reduce()`.

Aquí está cómo se puede hacer:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Copia y pega el siguiente código:

```js
const countOccurrences = (arr, val) =>
  arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
```

3. En el código anterior, la función `countOccurrences` toma dos argumentos: la matriz en la que buscar y el valor que se va a contar.
4. El método `reduce()` se utiliza para recorrer cada elemento de la matriz y aumentar un contador cada vez que se encuentra el valor específico.
5. Para probar la función, llámala con una matriz y un valor, como esto:

```js
countOccurrences([1, 1, 2, 1, 2, 3], 1); // 3
```

Esto devolverá el número de veces que `1` aparece en la matriz `[1, 1, 2, 1, 2, 3]`, que es `3`.
