# Comment appeler des fonctions avec un contexte en JavaScript

Pour exécuter du code dans Node.js, ouvrez le Terminal/SSH et tapez `node`. Si vous voulez appeler une fonction avec un contexte spécifique et un ensemble d'arguments en JavaScript, vous pouvez utiliser une fermeture. Voici comment faire :

1. Définissez une fonction appelée `call` qui prend une `clé` et un ensemble d'`arguments` en tant que paramètres et renvoie une nouvelle fonction qui prend un paramètre `contexte`.

```js
const call =
  (key, ...args) =>
  (context) =>
    context[key](...args);
```

2. Utilisez la fonction `call` pour appeler la fonction `map` sur un tableau de nombres. Dans cet exemple, la fonction `map` double chaque nombre du tableau.

```js
Promise.resolve([1, 2, 3])
  .then(call("map", (x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

3. Vous pouvez également lier la fonction `call` à une clé spécifique, telle que `map`, et l'utiliser pour appeler la fonction `map` sur un tableau de nombres.

```js
const map = call.bind(null, "map");
Promise.resolve([1, 2, 3])
  .then(map((x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

En utilisant la fonction `call`, vous pouvez facilement appeler n'importe quelle fonction avec un contexte spécifique et un ensemble d'arguments.
