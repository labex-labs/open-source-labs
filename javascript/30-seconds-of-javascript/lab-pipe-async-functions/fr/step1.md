# Comment utiliser les fonctions asynchrones en chaîne en JavaScript

Pour commencer à coder avec JavaScript, ouvrez le Terminal/SSH et tapez `node`. Une fois que vous êtes familier avec les bases, vous pouvez commencer à travailler avec les fonctions asynchrones.

La fonction `pipeAsyncFunctions` vous permet d'effectuer une composition de fonctions de gauche à droite avec des fonctions asynchrones. Voici comment elle fonctionne :

- La fonction prend un nombre quelconque de fonctions asynchrones en arguments.
- L'opérateur de répandue (`...`) est utilisé pour passer ces fonctions en tant qu'arguments séparés à la fonction `pipeAsyncFunctions`.
- La fonction résultante peut accepter un nombre quelconque d'arguments, mais chacune des fonctions composées doit accepter un seul argument.
- Les fonctions peuvent renvoyer une combinaison de valeurs normales, de Promesses, ou être `async` et renvoyer via `await`.
- La méthode `reduce()` est utilisée avec `Promise.prototype.then()` pour effectuer la composition de fonctions.
- La méthode `reduce()` itère sur les fonctions, les exécutant l'une après l'autre et passant le résultat d'une fonction à la suivante.
- La Promesse résultante est renvoyée.

Voici un exemple de manière d'utiliser `pipeAsyncFunctions` pour additionner un nombre :

```js
const sum = pipeAsyncFunctions(
  (x) => x + 1,
  (x) => new Promise((resolve) => setTimeout(() => resolve(x + 2), 1000)),
  (x) => x + 3,
  async (x) => (await x) + 4
);
(async () => {
  console.log(await sum(5)); // 15 (après une seconde)
})();
```

Dans cet exemple, `sum` est composée de quatre fonctions qui ajoutent des valeurs différentes au nombre d'entrée. La valeur finale de `sum` est le résultat de l'exécution de chaque fonction dans l'ordre, avec un délai d'une seconde pour la deuxième fonction. Le mot clé `async` est utilisé avec la dernière fonction pour autoriser l'utilisation de `await`.

En utilisant `pipeAsyncFunctions`, vous pouvez facilement composer un nombre quelconque de fonctions asynchrones ensemble pour créer une fonctionnalité plus complexe.
