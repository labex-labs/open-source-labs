# Arguments de fonction ajoutés avec Partial

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et entrez `node`.

La fonction `partial` est utilisée pour créer une nouvelle fonction qui appelle `fn` avec `partials` comme premiers arguments.

- Utilisez l'opérateur de propagation (`...`) pour ajouter `partials` à la liste d'arguments de `fn`.

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
