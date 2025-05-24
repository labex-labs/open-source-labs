# Sequência de Fibonacci

Para gerar a sequência de Fibonacci em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node`.
2.  Use `Array.from()` para criar um array vazio do comprimento específico, inicializando os dois primeiros valores (`0` e `1`).
3.  Use `Array.prototype.reduce()` e `Array.prototype.concat()` para adicionar valores ao array, usando a soma dos dois últimos valores, exceto para os dois primeiros.
4.  Chame a função `fibonacci()` e passe o comprimento desejado da sequência como um argumento.

Aqui está o código:

```js
const fibonacci = (n) =>
  Array.from({ length: n }).reduce(
    (acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
    []
  );

fibonacci(6); // [0, 1, 1, 2, 3, 5]
```

Isso gerará um array contendo a sequência de Fibonacci até o n-ésimo termo.
