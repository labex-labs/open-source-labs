# Composição de Funções com Pipes

Para começar a praticar a codificação com pipes, abra o Terminal/SSH e digite `node`.

A função `pipeFunctions` realiza a composição de funções da esquerda para a direita usando `Array.prototype.reduce()` com o operador spread (`...`). A primeira função (mais à esquerda) pode aceitar um ou mais argumentos, enquanto as funções restantes devem ser unárias.

```js
const pipeFunctions = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

Aqui está um exemplo de como usar `pipeFunctions` para criar uma nova função `multiplyAndAdd5` que multiplica dois números e, em seguida, adiciona 5 ao resultado:

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
const multiplyAndAdd5 = pipeFunctions(multiply, add5);
multiplyAndAdd5(5, 2); // 15
```

Neste exemplo, `multiplyAndAdd5` é uma nova função que recebe dois argumentos, `5` e `2`, e aplica `multiply` a eles primeiro, resultando em `10`, e então aplica `add5` ao resultado, resultando em `15`.
