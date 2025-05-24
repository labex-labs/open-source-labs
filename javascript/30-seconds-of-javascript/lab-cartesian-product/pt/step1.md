# Produto Cartesiano (Cartesian Product)

Para calcular o produto cartesiano de dois arrays, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.reduce()`, `Array.prototype.map()` e o operador spread (`...`) para gerar todos os pares de elementos possíveis a partir dos dois arrays.
3. Use o seguinte código:

```js
const cartesianProduct = (a, b) =>
  a.reduce((p, x) => [...p, ...b.map((y) => [x, y])], []);
```

Exemplo:

```js
cartesianProduct(["x", "y"], [1, 2]);
// [['x', 1], ['x', 2], ['y', 1], ['y', 2]]
```

Isso gerará todas as combinações possíveis de elementos dos dois arrays.
