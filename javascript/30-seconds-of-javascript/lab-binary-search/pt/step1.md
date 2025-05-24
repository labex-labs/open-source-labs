# Algoritmo de Busca Binária (Binary Search Algorithm)

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`. O algoritmo de busca binária é usado para encontrar o índice de um determinado elemento em um array ordenado. Aqui estão os passos para implementar o algoritmo de busca binária:

1.  Declare os limites de busca à esquerda e à direita, `l` e `r`, inicializados em `0` e no `length` (comprimento) do array, respectivamente.
2.  Use um loop `while` para reduzir repetidamente o subarray de busca, dividindo-o pela metade usando `Math.floor()`.
3.  Se o elemento for encontrado, retorne seu índice. Caso contrário, retorne `-1`.
4.  Observe que este algoritmo não considera valores duplicados no array.

Aqui está um exemplo de implementação do algoritmo de busca binária em JavaScript:

```js
const binarySearch = (arr, item) => {
  let l = 0,
    r = arr.length - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    const guess = arr[mid];
    if (guess === item) return mid;
    if (guess > item) r = mid - 1;
    else l = mid + 1;
  }
  return -1;
};
```

Você pode testar a função `binarySearch` com os seguintes exemplos:

```js
binarySearch([1, 2, 3, 4, 5], 1); // 0
binarySearch([1, 2, 3, 4, 5], 5); // 4
binarySearch([1, 2, 3, 4, 5], 6); // -1
```
