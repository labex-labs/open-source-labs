# Verificar se um Valor é uma Função Assíncrona em JavaScript

Para verificar se um valor é uma função `async` em JavaScript, você pode usar o seguinte código:

```js
const isAsyncFunction = (val) =>
  Object.prototype.toString.call(val) === "[object AsyncFunction]";
```

Esta função usa `Object.prototype.toString()` e `Function.prototype.call()` para verificar se o argumento fornecido é uma função `async`.

Você pode testar a função passando uma função regular e uma função `async` como argumentos:

```js
isAsyncFunction(function () {}); // false
isAsyncFunction(async function () {}); // true
```

Para começar a praticar a codificação em JavaScript, abra o Terminal/SSH e digite `node`.
