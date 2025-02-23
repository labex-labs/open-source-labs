# Argumentos de función prependidos con Partial

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

La función `partial` se utiliza para crear una nueva función que llama a `fn` con `partials` como los primeros argumentos.

- Utiliza el operador de propagación (`...`) para prepender `partials` a la lista de argumentos de `fn`.

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
