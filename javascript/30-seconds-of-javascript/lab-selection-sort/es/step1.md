# Algoritmo de selección

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

La siguiente función ordena una matriz de números utilizando el algoritmo de selección:

```js
const selectionSort = (arr) => {
  const a = [...arr];
  for (let i = 0; i < a.length; i++) {
    const min = a
      .slice(i + 1)
      .reduce((acc, val, j) => (val < a[acc] ? j + i + 1 : acc), i);
    if (min !== i) [a[i], a[min]] = [a[min], a[i]];
  }
  return a;
};
```

Para usar la función, pasa una matriz de números a `selectionSort()`, así:

```js
selectionSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```

La función funciona clonando la matriz original utilizando el operador de propagación (`...`). Luego itera sobre la matriz utilizando un bucle `for`. Utilizando `Array.prototype.slice()` y `Array.prototype.reduce()`, encuentra el índice del elemento mínimo en la submatriz a la derecha del índice actual. Si es necesario, realiza un intercambio.
