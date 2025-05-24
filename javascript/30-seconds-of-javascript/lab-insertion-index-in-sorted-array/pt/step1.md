# Como Encontrar o Índice de Inserção em um Array Ordenado

Para encontrar o índice mais baixo no qual um valor deve ser inserido em um array ordenado, siga estes passos:

1.  Verifique se o array está ordenado em ordem decrescente.
2.  Use o método `Array.prototype.findIndex()` para encontrar o índice apropriado onde o elemento deve ser inserido.

Aqui está o código para implementar isso:

```js
const sortedIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr.findIndex((el) => (isDescending ? n >= el : n <= el));
  return index === -1 ? arr.length : index;
};
```

Você pode chamar a função `sortedIndex` passando o array ordenado e o valor que deseja inserir. Aqui estão alguns exemplos:

```js
sortedIndex([5, 3, 2, 1], 4); // Output: 1
sortedIndex([30, 50], 40); // Output: 1
```

Ao usar esta função, você pode facilmente encontrar o índice de inserção de um valor em um array ordenado.
