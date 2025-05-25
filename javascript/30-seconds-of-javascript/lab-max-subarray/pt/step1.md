# Algoritmo de Subarray Máximo

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Este algoritmo encontra um subarray contíguo com a maior soma dentro de um array de números. Para implementar este algoritmo, siga estes passos:

- Use uma abordagem _greedy_ (gananciosa) para acompanhar a `sum` (soma) atual e o máximo atual, `maxSum`. Defina `maxSum` como `-Infinity` para garantir que o maior valor negativo seja retornado, se todos os valores forem negativos.
- Defina variáveis para acompanhar o índice inicial máximo, `sMax`, o índice final máximo, `eMax`, e o índice inicial atual, `s`.
- Use `Array.prototype.forEach()` para iterar sobre os valores e adicionar o valor atual à `sum`.
- Se a `sum` atual for maior que `maxSum`, atualize os valores dos índices e o `maxSum`.
- Se a `sum` estiver abaixo de `0`, reinicie-a para `0` e atualize o valor de `s` para o próximo índice.
- Use `Array.prototype.slice()` para retornar o subarray indicado pelas variáveis de índice.

Aqui está o código JavaScript para o algoritmo:

```js
const maxSubarray = (...arr) => {
  let maxSum = -Infinity,
    sum = 0;
  let sMax = 0,
    eMax = arr.length - 1,
    s = 0;

  arr.forEach((n, i) => {
    sum += n;
    if (maxSum < sum) {
      maxSum = sum;
      sMax = s;
      eMax = i;
    }

    if (sum < 0) {
      sum = 0;
      s = i + 1;
    }
  });

  return arr.slice(sMax, eMax + 1);
};
```

Aqui está um exemplo de como usar a função:

```js
maxSubarray(-2, 1, -3, 4, -1, 2, 1, -5, 4); // [4, -1, 2, 1]
```
