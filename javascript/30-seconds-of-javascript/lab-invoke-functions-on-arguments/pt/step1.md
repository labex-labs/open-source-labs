# Invocando Funções com Argumentos

Para executar código usando Node.js, abra o Terminal/SSH e digite `node`.

Para criar uma função que invoca cada função fornecida com os argumentos que recebe e retorna os resultados:

- Use `Array.prototype.map()` e `Function.prototype.apply()` para aplicar cada função aos argumentos fornecidos.

```js
const over =
  (...fns) =>
  (...args) =>
    fns.map((fn) => fn.apply(null, args));
```

Exemplo:

```js
const minMax = over(Math.min, Math.max);
minMax(1, 2, 3, 4, 5); // [1, 5]
```
