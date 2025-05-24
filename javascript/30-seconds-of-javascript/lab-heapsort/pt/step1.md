# Algoritmo Heap Sort

Para praticar a codificação, abra o Terminal/SSH e digite 'node'. O seguinte algoritmo ordena um array de números usando o algoritmo heapsort. Siga estes passos:

- Use recursão na função.
- Use o operador spread `(...)` para clonar o array original, `arr`.
- Use closures para declarar uma variável, `l`, e uma função `heapify`.
- Use um loop `for` e `Math.floor()` em combinação com `heapify` para criar um max heap a partir do array.
- Use um loop `for` para reduzir repetidamente o intervalo considerado, usando `heapify` e trocando valores conforme necessário para ordenar o array clonado.

```js
const heapsort = (arr) => {
  const a = [...arr];
  let l = a.length;
  const heapify = (a, i) => {
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    let max = i;
    if (left < l && a[left] > a[max]) max = left;
    if (right < l && a[right] > a[max]) max = right;
    if (max !== i) {
      [a[max], a[i]] = [a[i], a[max]];
      heapify(a, max);
    }
  };
  for (let i = Math.floor(l / 2); i >= 0; i -= 1) heapify(a, i);
  for (let i = a.length - 1; i > 0; i--) {
    [a[0], a[i]] = [a[i], a[0]];
    l--;
    heapify(a, 0);
  }
  return a;
};
```

Por exemplo:

```js
heapsort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
