# Uma Função para Encontrar a Diferença Simétrica de Arrays

Para encontrar a diferença simétrica entre dois arrays usando uma função fornecida como comparador, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use os métodos `Array.prototype.filter()` e `Array.prototype.findIndex()` para encontrar os valores apropriados.
3.  Use o código fornecido para realizar a operação.

```js
const symmetricDifferenceWith = (arr, val, comp) => [
  ...arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1),
  ...val.filter((a) => arr.findIndex((b) => comp(a, b)) === -1)
];
```

Por exemplo, considere a seguinte entrada:

```js
symmetricDifferenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
); // [1, 1.2, 3.9]
```

O código acima retornará `[1, 1.2, 3.9]` como a diferença simétrica entre os dois arrays.
