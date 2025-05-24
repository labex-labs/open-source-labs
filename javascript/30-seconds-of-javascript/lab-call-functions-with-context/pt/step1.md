# Como Chamar Funções com Contexto em JavaScript

Para executar código em Node.js, abra o Terminal/SSH e digite `node`. Se você deseja chamar uma função com um contexto específico e um conjunto de argumentos em JavaScript, pode usar uma _closure_. Veja como você pode fazer isso:

1.  Defina uma função chamada `call` que recebe uma `key` e um conjunto de `args` como parâmetros e retorna uma nova função que recebe um parâmetro `context`.

```js
const call =
  (key, ...args) =>
  (context) =>
    context[key](...args);
```

2.  Use a função `call` para chamar a função `map` em um array de números. Neste exemplo, a função `map` duplica cada número no array.

```js
Promise.resolve([1, 2, 3])
  .then(call("map", (x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

3.  Você também pode associar a função `call` a uma chave específica, como `map`, e usá-la para chamar a função `map` em um array de números.

```js
const map = call.bind(null, "map");
Promise.resolve([1, 2, 3])
  .then(map((x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

Ao usar a função `call`, você pode facilmente chamar qualquer função com um contexto específico e um conjunto de argumentos.
