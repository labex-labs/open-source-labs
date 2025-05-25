# Algoritmo Quick Sort

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Este algoritmo ordena um array de números usando o algoritmo quicksort. Aqui estão os passos a seguir:

- Use recursão.
- Use o operador spread (`...`) para clonar o array original, `arr`.
- Se o `length` do array for menor que `2`, retorne o array clonado.
- Use `Math.floor()` para calcular o índice do elemento pivô (pivot).
- Use `Array.prototype.reduce()` e `Array.prototype.push()` para dividir o array em dois subarrays. O primeiro contém elementos menores ou iguais ao `pivot`, e o segundo contém elementos maiores que ele. Desestruture o resultado em dois arrays.
- Chame recursivamente `quickSort()` nos subarrays criados.

Aqui está um exemplo de como implementar este algoritmo:

```js
const quickSort = (arr) => {
  const a = [...arr];
  if (a.length < 2) return a;
  const pivotIndex = Math.floor(arr.length / 2);
  const pivot = a[pivotIndex];
  const [lo, hi] = a.reduce(
    (acc, val, i) => {
      if (val < pivot || (val === pivot && i != pivotIndex)) {
        acc[0].push(val);
      } else if (val > pivot) {
        acc[1].push(val);
      }
      return acc;
    },
    [[], []]
  );
  return [...quickSort(lo), pivot, ...quickSort(hi)];
};
```

Para testá-lo, execute o seguinte comando:

```js
quickSort([1, 6, 1, 5, 3, 2, 1, 4]); // [1, 1, 1, 2, 3, 4, 5, 6]
```
