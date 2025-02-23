# Fonction promisify

Pour convertir une fonction asynchrone pour qu'elle renvoie une promesse, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la curry pour renvoyer une fonction qui renvoie une `Promise` qui appelle la fonction d'origine.
3. Utilisez l'opérateur rest (`...`) pour passer tous les paramètres.
4. Si vous utilisez Node 8+, vous pouvez utiliser [`util.promisify`](https://nodejs.org/api/util.html#util_util_promisify_original).
5. Voici un extrait de code d'exemple :

```js
const promisify =
  (func) =>
  (...args) =>
    new Promise((resolve, reject) =>
      func(...args, (err, result) => (err ? reject(err) : resolve(result)))
    );
```

6. Pour utiliser cette fonction, définissez la fonction asynchrone et passez-la en tant que paramètre à la fonction `promisify`. La fonction renvoyée renverra désormais une promesse.

```js
const delay = promisify((d, cb) => setTimeout(cb, d));
delay(2000).then(() => console.log("Hi!")); // La promesse est résolue après 2 s
```

La fonction `delay` est un exemple d'une fonction asynchrone qui renvoie désormais une promesse à l'aide de la fonction `promisify`.
