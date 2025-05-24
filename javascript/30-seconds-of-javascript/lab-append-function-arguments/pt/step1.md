# Função que Anexa Argumentos

Para criar uma função que anexa argumentos aos que recebe, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador spread (`...`) para anexar `partials` à lista de argumentos de `fn`.
3.  Use o seguinte código para criar a função:

```js
const partialRight =
  (fn, ...partials) =>
  (...args) =>
    fn(...args, ...partials);
```

4.  Teste a função com um exemplo, como:

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetJohn = partialRight(greet, "John");
greetJohn("Hello"); // 'Hello John!'
```
