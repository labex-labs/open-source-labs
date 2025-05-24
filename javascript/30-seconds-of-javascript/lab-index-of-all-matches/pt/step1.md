# Índice de Todas as Correspondências

Para encontrar todos os índices de `val` em um array, use `Array.prototype.reduce()` para iterar sobre os elementos e armazenar os índices dos elementos correspondentes. Se `val` nunca ocorrer, um array vazio é retornado.

```js
const indexOfAll = (arr, val) =>
  arr.reduce((acc, el, i) => (el === val ? [...acc, i] : acc), []);
```

Exemplo de uso:

```js
indexOfAll([1, 2, 3, 1, 2, 3], 1); // [0, 3]
indexOfAll([1, 2, 3], 4); // []
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Este é um índice de todas as correspondências.
