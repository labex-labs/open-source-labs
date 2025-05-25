# Descrição do Último Índice de Inserção em Array Ordenado

Para encontrar o índice mais alto onde um valor deve ser inserido em um array a fim de manter sua ordem de classificação, siga estes passos:

- Primeiro, verifique superficialmente se o array está ordenado em ordem decrescente.
- Em seguida, use `Array.prototype.reverse()` e `Array.prototype.findIndex()` para encontrar o último índice apropriado onde o elemento deve ser inserido.

Aqui está o código da função:

```js
const sortedLastIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr
    .reverse()
    .findIndex((el) => (isDescending ? n <= el : n >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

E aqui está um exemplo de como usar a função:

```js
sortedLastIndex([10, 20, 30, 30, 40], 30); // 4
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
