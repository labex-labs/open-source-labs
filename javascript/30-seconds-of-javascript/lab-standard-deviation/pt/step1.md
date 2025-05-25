# Desvio Padrão (Standard Deviation)

Para calcular o desvio padrão de um array de números em JavaScript, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use a função `standardDeviation(arr, usePopulation = false)` fornecida abaixo.
3. Passe um array de números como o primeiro argumento para a função.
4. Omita o segundo argumento, `usePopulation`, para obter o desvio padrão amostral. Defina-o como `true` para obter o desvio padrão populacional.

```js
const standardDeviation = (arr, usePopulation = false) => {
  const mean = arr.reduce((acc, val) => acc + val, 0) / arr.length;
  return Math.sqrt(
    arr
      .reduce((acc, val) => acc.concat((val - mean) ** 2), [])
      .reduce((acc, val) => acc + val, 0) /
      (arr.length - (usePopulation ? 0 : 1))
  );
};
```

Exemplo de uso:

```js
standardDeviation([10, 2, 38, 23, 38, 23, 21]); // 13.284434142114991 (sample)
standardDeviation([10, 2, 38, 23, 38, 23, 21], true); // 12.29899614287479 (population)
```
