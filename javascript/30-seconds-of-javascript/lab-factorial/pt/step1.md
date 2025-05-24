# Calculando o Fatorial de um Número

Para calcular o fatorial de um número, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use recursão para calcular o fatorial.
3.  Se `n` for menor ou igual a `1`, retorne `1`.
4.  Caso contrário, retorne o produto de `n` e o fatorial de `n - 1`.
5.  Se `n` for um número negativo, lance um `TypeError`.

Aqui está o código para calcular o fatorial:

```js
const factorial = (n) =>
  n < 0
    ? (() => {
        throw new TypeError("Negative numbers are not allowed!");
      })()
    : n <= 1
      ? 1
      : n * factorial(n - 1);
```

Você pode testar o código chamando a função `factorial` com um número como argumento:

```js
factorial(6); // 720
```
