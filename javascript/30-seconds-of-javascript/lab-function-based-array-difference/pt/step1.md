# Como Filtrar Valores de um Array com Base em uma Função

Para filtrar todos os valores de um array com base em uma função comparadora fornecida, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.filter()` e `Array.prototype.findIndex()` para encontrar os valores apropriados.
3. Omita o último argumento, `comp`, para usar um comparador de igualdade estrita padrão.
4. Use o seguinte código:

```js
const differenceWith = (arr, val, comp = (a, b) => a === b) =>
  arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1);
```

5. Teste sua função com os seguintes exemplos:

```js
differenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0],
  (a, b) => Math.round(a) === Math.round(b)
); // Expected output: [1, 1.2]

differenceWith([1, 1.2, 1.3], [1, 1.3, 1.5]); // Expected output: [1.2]
```
