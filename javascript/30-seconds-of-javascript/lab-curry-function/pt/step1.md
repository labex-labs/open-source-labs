# _Currying_ de uma Função

Para fazer _currying_ de uma função, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use recursão.
3. Verifique se o número de argumentos fornecidos (`args`) é suficiente.
4. Se sim, chame a função passada `fn`.
5. Se não, use `Function.prototype.bind()` para retornar uma função _curried_ `fn` que espera o restante dos argumentos.
6. Se você deseja fazer _currying_ de uma função que aceita um número variável de argumentos (uma função variádica, por exemplo, `Math.min()`), você pode opcionalmente passar o número de argumentos para o segundo parâmetro `arity`.
7. Use o seguinte código:

```js
const curry = (fn, arity = fn.length, ...args) =>
  arity <= args.length ? fn(...args) : curry.bind(null, fn, arity, ...args);
```

Aqui estão alguns exemplos:

```js
curry(Math.pow)(2)(10); // 1024
curry(Math.min, 3)(10)(50)(2); // 2
```
