# Como Atrasar a Execução de Funções em JavaScript

Para atrasar a execução de uma função em JavaScript, você pode usar o método `setTimeout()`. Veja como fazer:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a seguinte sintaxe para atrasar a execução de uma função `fn` por `ms` milissegundos:

```js
const delay = (fn, ms, ...args) => setTimeout(fn, ms, ...args);
```

3.  Para passar argumentos para a função, use o operador spread (`...`) desta forma:

```js
delay(
  function (text) {
    console.log(text);
  },
  1000,
  "later"
); // Logs 'later' after one second.
```

Com este código, a função `fn` fornecida será invocada após o número especificado de milissegundos (`ms`). O parâmetro `...args` permite que você passe um número arbitrário de argumentos para a função.
