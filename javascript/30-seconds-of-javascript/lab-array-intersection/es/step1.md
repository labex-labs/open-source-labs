# Encontrar la intersección de arrays

Para encontrar los elementos comunes entre dos arrays y eliminar los duplicados, utiliza el siguiente código:

```js
const intersection = (arr1, arr2) => {
  const set = new Set(arr2);
  return [...new Set(arr1)].filter((elem) => set.has(elem));
};
```

Para utilizar este código, abre la Terminal/SSH y escribe `node`. Luego, llama a la función `intersection` con dos arrays como argumentos, así:

```js
intersection([1, 2, 3], [4, 3, 2]); // [2, 3]
```

Esto devolverá un array que contiene los elementos que existen en ambos arrays, con los duplicados eliminados.
