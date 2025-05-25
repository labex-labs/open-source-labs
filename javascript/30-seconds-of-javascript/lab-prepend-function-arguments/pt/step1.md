# Argumentos de Função Adicionados no Início com Partial

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

A função `partial` é usada para criar uma nova função que chama `fn` com `partials` como os primeiros argumentos.

- Use o operador spread (`...`) para adicionar `partials` no início da lista de argumentos de `fn`.

```js
const partial =
  (fn, ...partials) =>
  (...args) =>
    fn(...partials, ...args);
```

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetHello = partial(greet, "Hello");
greetHello("John"); // 'Hello John!'
```
