# Como Encontrar o Último Índice de Inserção em um Array Ordenado com Base em uma Função

Para começar a codificar, abra o Terminal/SSH e digite `node`.

Aqui está como encontrar o índice mais alto no qual um valor deve ser inserido em um array para manter sua ordem de classificação, com base em uma função iteradora fornecida:

1. Verifique se o array está ordenado em ordem decrescente.
2. Use `Array.prototype.map()` para aplicar a função iteradora a todos os elementos do array.
3. Use `Array.prototype.reverse()` e `Array.prototype.findIndex()` para encontrar o último índice apropriado onde o elemento deve ser inserido, com base na função iteradora fornecida.

Veja o código abaixo:

```js
const sortedLastIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr
    .map(fn)
    .reverse()
    .findIndex((el) => (isDescending ? val <= el : val >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

Aqui está um exemplo:

```js
sortedLastIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, (o) => o.x); // 1
```
