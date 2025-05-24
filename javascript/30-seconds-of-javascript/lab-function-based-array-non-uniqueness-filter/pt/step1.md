# Filtrando Valores Não Únicos de um Array com uma Função

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Este código filtra valores não únicos de um array, com base em uma função comparadora fornecida. Aqui estão os passos para alcançar isso:

1.  Use `Array.prototype.filter()` e `Array.prototype.every()` para criar um novo array com apenas os valores únicos com base na função comparadora `fn`.
2.  A função comparadora recebe quatro argumentos: os valores dos dois elementos sendo comparados e seus índices.
3.  A função `filterNonUniqueBy` implementa os passos acima e retorna o array de valores únicos.

```js
const filterNonUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.every((x, j) => (i === j) === fn(v, x, i, j)));
```

Aqui está um exemplo de como usar esta função:

```js
filterNonUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id === b.id
); // [ { id: 2, value: 'c' } ]
```

Este código é conciso, claro e coerente e deve funcionar como esperado.
