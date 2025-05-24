# Como Compor Funções em JavaScript

Para começar a praticar a codificação usando a composição de funções em JavaScript, abra o Terminal/SSH e digite `node`.

Aqui está um exemplo de como realizar a composição de funções da direita para a esquerda em JavaScript:

1.  Use `Array.prototype.reduce()` para realizar a composição de funções da direita para a esquerda.
2.  A última função (mais à direita) pode aceitar um ou mais argumentos; as funções restantes devem ser unárias.
3.  Defina a função `compose` que receberá qualquer número de funções como argumentos e retornará uma nova função que as compõe.
4.  Chame a função `compose` com as funções desejadas na ordem desejada.
5.  Chame a nova função composta com quaisquer argumentos necessários.

```js
const compose = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args))
  );
```

Por exemplo, digamos que temos duas funções:

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
```

Podemos compor essas funções usando `compose`:

```js
const multiplyAndAdd5 = compose(add5, multiply);
```

Agora podemos chamar `multiplyAndAdd5` com os argumentos desejados:

```js
multiplyAndAdd5(5, 2); // 15
```
