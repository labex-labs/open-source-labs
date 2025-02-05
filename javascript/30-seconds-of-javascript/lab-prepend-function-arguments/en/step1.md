# Function Arguments Prepended with Partial

To begin practicing coding, open the Terminal/SSH and enter `node`.

The function `partial` is used to create a new function that calls `fn` with `partials` as the first arguments.

- Use the spread operator (`...`) to prepend `partials` to the list of arguments of `fn`.

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
