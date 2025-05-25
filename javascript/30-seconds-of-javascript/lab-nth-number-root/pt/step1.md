# Como Calcular a Raiz N-ésima de um Número

Para calcular a raiz n-ésima de um número:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a fórmula `Math.pow(x, 1/n)` para calcular `x` elevado à potência de `1/n`.
3.  O resultado deste cálculo é igual à raiz n-ésima de `x`.

Aqui está um exemplo de trecho de código:

```js
const nthRoot = (x, n) => Math.pow(x, 1 / n);
nthRoot(32, 5); // Output: 2
```

Este código calculará a raiz n-ésima de 32 (onde n é 5) e retornará a saída como 2.
