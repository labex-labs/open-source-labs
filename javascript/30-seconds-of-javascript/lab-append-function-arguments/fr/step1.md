# Fonction qui ajoute des arguments

Pour créer une fonction qui ajoute des arguments à ceux qu'elle reçoit, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer la pratique de codage.
2. Utilisez l'opérateur de propagation (`...`) pour ajouter `partials` à la liste d'arguments de `fn`.
3. Utilisez le code suivant pour créer la fonction :

```js
const partialRight =
  (fn, ...partials) =>
  (...args) =>
    fn(...args, ...partials);
```

4. Testez la fonction avec un exemple, tel que :

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetJohn = partialRight(greet, "John");
greetJohn("Hello"); // 'Hello John!'
```
