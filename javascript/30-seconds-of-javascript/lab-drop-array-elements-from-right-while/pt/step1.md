# Removendo Elementos de um Array da Direita com Base em uma Função

Para remover elementos do final de um array até que uma determinada condição seja atendida, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Itere sobre o array usando `Array.prototype.slice()` para remover o último elemento do array até que a `func` passada retorne `true`.
3. Retorne os elementos restantes no array.

Aqui está um exemplo de implementação:

```js
const dropRightWhile = (arr, func) => {
  let rightIndex = arr.length;
  while (rightIndex-- && !func(arr[rightIndex]));
  return arr.slice(0, rightIndex + 1);
};
```

Você pode usar esta função da seguinte forma:

```js
dropRightWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
