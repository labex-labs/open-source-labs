# Invertendo a Composição de Funções

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está como realizar a composição de funções da esquerda para a direita:

- Use o método `Array.prototype.reduce()` para realizar a composição de funções da esquerda para a direita.
- A primeira função (mais à esquerda) pode aceitar um ou mais argumentos, enquanto as funções restantes devem ser unárias.

```js
const composeRight = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

Por exemplo:

```js
const add = (x, y) => x + y;
const square = (x) => x * x;
const addAndSquare = composeRight(add, square);
addAndSquare(1, 2); // 9
```
