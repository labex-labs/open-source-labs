# Algoritmo de Ordenação por Seleção (Selection Sort)

Para começar a codificar, abra o Terminal/SSH e digite `node`.

A seguinte função ordena um array de números usando o algoritmo de ordenação por seleção:

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

Para usar a função, passe um array de números para `selectionSort()`, assim:

```js
selectionSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```

A função funciona clonando o array original usando o operador spread (`...`). Em seguida, itera sobre o array usando um loop `for`. Usando `Array.prototype.slice()` e `Array.prototype.reduce()`, ela encontra o índice do elemento mínimo no subarray à direita do índice atual. Se necessário, realiza uma troca (swap).
