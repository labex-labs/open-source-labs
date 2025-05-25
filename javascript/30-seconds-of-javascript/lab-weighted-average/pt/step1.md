# Como Calcular a Média Ponderada em JavaScript

Para calcular a média ponderada de dois ou mais números em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.reduce()` para criar a soma ponderada dos valores e a soma dos pesos.
3.  Divida a soma ponderada dos valores pela soma dos pesos para obter a média ponderada.

Aqui está o código JavaScript para a função `weightedAverage`:

```js
const weightedAverage = (nums, weights) => {
  const [sum, weightSum] = weights.reduce(
    (acc, w, i) => {
      acc[0] = acc[0] + nums[i] * w;
      acc[1] = acc[1] + w;
      return acc;
    },
    [0, 0]
  );
  return sum / weightSum;
};
```

Você pode usar a função `weightedAverage` para calcular a média ponderada de um array de números e um array de pesos assim:

```js
weightedAverage([1, 2, 3], [0.6, 0.2, 0.3]); // 1.72727
```
