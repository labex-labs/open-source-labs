# Funções Convergentes

Para praticar a codificação, abra o Terminal/SSH e digite `node`.

Esta função `converge` recebe uma função convergente e uma lista de funções de ramificação como entrada. Ela retorna uma nova função que aplica cada função de ramificação aos argumentos de entrada. Os resultados das funções de ramificação são então passados como argumentos para a função convergente.

Os métodos `Array.prototype.map()` e `Function.prototype.apply()` são usados para aplicar cada função aos argumentos de entrada. O operador spread (`...`) é então usado para chamar `converger` com os resultados de todas as outras funções.

Aqui está o código para a função `converge`:

```js
const converge =
  (converger, fns) =>
  (...args) =>
    converger(...fns.map((fn) => fn.apply(null, args)));
```

Um exemplo de como usar esta função é mostrado abaixo. A função `average` é criada chamando `converge` com uma função anônima que calcula a média de um array. As funções de ramificação são duas funções anônimas que calculam a soma de um array e seu comprimento, respectivamente.

```js
const average = converge(
  (a, b) => a / b,
  [(arr) => arr.reduce((a, v) => a + v, 0), (arr) => arr.length]
);
average([1, 2, 3, 4, 5, 6, 7]); // 4
```

Este código calcula a média do array `[1, 2, 3, 4, 5, 6, 7]` e retorna `4`.
