# Função Promisify

Para converter uma função assíncrona para retornar uma _promise_, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use _currying_ para retornar uma função que retorna uma `Promise` que chama a função original.
3.  Use o operador _rest_ (`...`) para passar todos os parâmetros.
4.  Se você estiver usando Node 8+, pode usar [`util.promisify`](https://nodejs.org/api/util.html#util_util_promisify_original).
5.  Aqui está um exemplo de trecho de código:

```js
const promisify =
  (func) =>
  (...args) =>
    new Promise((resolve, reject) =>
      func(...args, (err, result) => (err ? reject(err) : resolve(result)))
    );
```

6.  Para usar esta função, defina a função assíncrona e passe-a como um parâmetro para a função `promisify`. A função retornada agora retornará uma _promise_.

```js
const delay = promisify((d, cb) => setTimeout(cb, d));
delay(2000).then(() => console.log("Hi!")); // Promise resolves after 2s
```

A função `delay` é um exemplo de uma função assíncrona que agora retorna uma _promise_ usando a função `promisify`.
