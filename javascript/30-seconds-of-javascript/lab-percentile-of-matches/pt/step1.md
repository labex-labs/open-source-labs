# Calculando a Percentila de Correspondências

Para calcular a percentila de correspondências no array fornecido abaixo, que são menores ou iguais a um determinado valor, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use o método `Array.prototype.reduce()` para calcular o número de valores abaixo do valor fornecido e o número de valores iguais ao valor fornecido.
3. Aplique a fórmula da percentila para obter a porcentagem de correspondências.
4. Aqui está um trecho de código de exemplo:

```js
const percentile = (arr, val) =>
  (100 *
    arr.reduce(
      (acc, v) => acc + (v < val ? 1 : 0) + (v === val ? 0.5 : 0),
      0
    )) /
  arr.length;
```

5. Para testar a função, use este código de exemplo:

```js
percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6); // Output: 55
```

Esta função irá gerar a porcentagem de correspondências no array fornecido que são menores ou iguais ao valor fornecido.
