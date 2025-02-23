# Mit Partial vorangestellte Funktionsargumente

Um zu beginnen, mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die Funktion `partial` wird verwendet, um eine neue Funktion zu erstellen, die `fn` mit `partials` als ersten Argumenten aufruft.

- Verwenden Sie den Spread-Operator (`...`), um `partials` der Argumentliste von `fn` voranzustellen.

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
