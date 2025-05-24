# Convertendo uma Função para uma Função Variádica

Para converter uma função que aceita um array em uma função variádica, você pode seguir estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2. Retorne uma closure (fechamento) que coleta todas as entradas em uma função que aceita um array.

```js
const collectInto =
  (fn) =>
  (...args) =>
    fn(args);
```

3. Use a função `collectInto` para converter uma função em uma função variádica.

```js
const Pall = collectInto(Promise.all.bind(Promise));
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(2);
let p3 = new Promise((resolve) => setTimeout(resolve, 2000, 3));
Pall(p1, p2, p3).then(console.log); // [1, 2, 3] (after about 2 seconds)
```

Isso permitirá que você aceite qualquer número de argumentos em sua função e os colete em um array para processamento posterior.
