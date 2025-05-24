# Cálculo do Coeficiente Binomial

Para calcular o número de maneiras de escolher `k` itens de `n` itens sem repetição e sem ordem, você pode usar a seguinte função JavaScript:

```js
const binomialCoefficient = (n, k) => {
  if (Number.isNaN(n) || Number.isNaN(k)) return NaN;
  if (k < 0 || k > n) return 0;
  if (k === 0 || k === n) return 1;
  if (k === 1 || k === n - 1) return n;
  if (n - k < k) k = n - k;
  let res = n;
  for (let j = 2; j <= k; j++) res *= (n - j + 1) / j;
  return Math.round(res);
};
```

Para usar a função, abra o Terminal/SSH e digite `node`. Em seguida, chame a função com os valores desejados. Por exemplo:

```js
binomialCoefficient(8, 2); // 28
```

Para garantir que a função funcione corretamente, você pode seguir estas etapas:

1. Use `Number.isNaN()` para verificar se algum dos dois valores é `NaN`.
2. Verifique se `k` é menor que `0`, maior ou igual a `n`, igual a `1` ou `n - 1` e retorne o resultado apropriado.
3. Verifique se `n - k` é menor que `k` e troque seus valores de acordo.
4. Faça um loop de `2` até `k` e calcule o coeficiente binomial.
5. Use `Math.round()` para contabilizar erros de arredondamento no cálculo.
