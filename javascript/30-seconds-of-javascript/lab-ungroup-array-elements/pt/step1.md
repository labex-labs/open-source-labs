# Como Desagrupar Elementos de Array em JavaScript

Para desagrupar os elementos em um array produzido pela função `zip`, você pode criar um array de arrays usando a função `unzip` em JavaScript. Veja como:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Math.max()`, `Function.prototype.apply()` para obter o subarray mais longo no array e `Array.prototype.map()` para transformar cada elemento em um array.
3.  Use `Array.prototype.reduce()` e `Array.prototype.forEach()` para mapear valores agrupados em arrays individuais.

Aqui está o código para a função `unzip`:

```js
const unzip = (arr) =>
  arr.reduce(
    (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
    Array.from({
      length: Math.max(...arr.map((x) => x.length))
    }).map((x) => [])
  );
```

Você pode usar a função `unzip` com os seguintes exemplos:

```js
unzip([
  ["a", 1, true],
  ["b", 2, false]
]); // [['a', 'b'], [1, 2], [true, false]]
unzip([
  ["a", 1, true],
  ["b", 2]
]); // [['a', 'b'], [1, 2], [true]]
```

Seguindo estas etapas, você pode facilmente desagrupar elementos de array em JavaScript.
