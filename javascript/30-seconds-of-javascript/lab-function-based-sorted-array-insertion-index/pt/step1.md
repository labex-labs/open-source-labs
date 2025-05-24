# Função para Encontrar o Índice de Inserção em um Array Ordenado

Para encontrar o índice mais baixo para inserir um valor em um array e manter sua ordem de classificação, use a função `sortedIndexBy(arr, n, fn)` em JavaScript.

Esta função verifica superficialmente se o array está ordenado em ordem decrescente e, em seguida, usa `Array.prototype.findIndex()` para encontrar o índice apropriado com base na função iteradora `fn`.

Aqui está o código para a função `sortedIndexBy()`:

```js
const sortedIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr.findIndex((el) =>
    isDescending ? val >= fn(el) : val <= fn(el)
  );
  return index === -1 ? arr.length : index;
};
```

Você pode chamar a função com um array de objetos, um valor para inserir e uma função iteradora.

Por exemplo, `sortedIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, o => o.x)` retorna `0`, que é o índice onde o objeto `{ x: 4 }` deve ser inserido para manter a ordem de classificação com base na propriedade `x`.
