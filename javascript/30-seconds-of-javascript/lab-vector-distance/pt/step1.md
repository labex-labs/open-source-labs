# Cálculo da Distância Vetorial

Para calcular a distância entre dois vetores, siga estes passos:

1.  Abra o Terminal/SSH para começar a praticar a codificação.
2.  Digite `node` para começar.
3.  Use `Array.prototype.reduce()`, `Math.pow()` e `Math.sqrt()` para encontrar a distância euclidiana entre os vetores.
4.  Aplique a fórmula `vectorDistance`, mostrada abaixo:

```js
const vectorDistance = (x, y) =>
  Math.sqrt(x.reduce((acc, val, i) => acc + Math.pow(val - y[i], 2), 0));
```

5.  Teste a fórmula inserindo dois vetores no seguinte formato: `vectorDistance([10, 0, 5], [20, 0, 10]);`
6.  A saída será a distância entre os dois vetores: `11.180339887498949`.
