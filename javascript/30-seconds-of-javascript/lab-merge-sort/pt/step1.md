# Algoritmo Merge Sort

Para praticar a codificação usando o algoritmo Merge Sort, siga estes passos:

1. Abra o Terminal/SSH e digite `node`.
2. Use recursão para ordenar um array de números.
3. Se o `length` (comprimento) do array for menor que `2`, retorne o array.
4. Use `Math.floor()` para calcular o ponto médio do array.
5. Use `Array.prototype.slice()` para dividir o array em dois e chame recursivamente `mergeSort()` nos subarrays criados.
6. Finalmente, use `Array.from()` e `Array.prototype.shift()` para combinar os dois subarrays ordenados em um só.

Aqui está o código:

```js
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const mid = Math.floor(arr.length / 2);
  const l = mergeSort(arr.slice(0, mid));
  const r = mergeSort(arr.slice(mid, arr.length));
  return Array.from({ length: l.length + r.length }, () => {
    if (!l.length) return r.shift();
    else if (!r.length) return l.shift();
    else return l[0] > r[0] ? r.shift() : l.shift();
  });
};
```

Experimente com este exemplo:

```js
mergeSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```
