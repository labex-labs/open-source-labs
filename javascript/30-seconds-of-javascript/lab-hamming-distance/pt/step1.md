# Cálculo da Distância de Hamming

Para calcular a distância de Hamming entre dois valores, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador XOR (`^`) para encontrar a diferença de bits entre os dois números.
3.  Converta o resultado para uma string binária usando `Number.prototype.toString()`.
4.  Conte o número de `1`s na string usando `String.prototype.match()`.
5.  Retorne a contagem.

Aqui está o código para a função `hammingDistance`:

```js
const hammingDistance = (num1, num2) =>
  ((num1 ^ num2).toString(2).match(/1/g) || "").length;
```

Você pode testar a função executando `hammingDistance(2, 3); // 1`.
