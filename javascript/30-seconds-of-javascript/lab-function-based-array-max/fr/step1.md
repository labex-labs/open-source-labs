# Comment trouver la valeur maximale d'un tableau en fonction d'une fonction

Pour trouver la valeur maximale d'un tableau en fonction d'une fonction, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.map()` pour mapper chaque élément du tableau à la valeur renvoyée par la fonction fournie, `fn`.
3. Utilisez `Math.max()` pour obtenir la valeur maximale du tableau mappé.

Voici un extrait de code d'exemple qui met en œuvre les étapes ci-dessus :

```js
const maxBy = (arr, fn) =>
  Math.max(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

Pour utiliser la fonction `maxBy`, passez un tableau et la fonction qui doit être utilisée pour mapper chaque élément à une valeur. Vous pouvez soit passer directement une fonction soit une chaîne de caractères représentant la clé qui doit être utilisée pour accéder à la valeur dans chaque objet du tableau.

Voici quelques appels d'exemple à la fonction `maxBy` :

```js
maxBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // renvoie 8
maxBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // renvoie 8
```
