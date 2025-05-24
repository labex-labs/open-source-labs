# Filtrar Valores Únicos de Array com Base em Função

Aqui está como criar um array que contém apenas os valores não únicos, filtrando os únicos com base em uma função comparadora, `fn`:

```js
const filterUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.some((x, j) => (i !== j) === fn(v, x, i, j)));
```

Para usar esta função, chame `filterUniqueBy()` com dois argumentos: o array que você deseja filtrar e a função comparadora. A função comparadora deve receber quatro argumentos: os valores dos dois elementos sendo comparados e seus índices.

Por exemplo, se você tiver um array de objetos e quiser filtrar os objetos com valores `id` únicos, você pode fazer isso:

```js
filterUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 3, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 0, value: 'e' } ]
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
