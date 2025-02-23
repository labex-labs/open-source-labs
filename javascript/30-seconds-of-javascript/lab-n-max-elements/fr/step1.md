# Comment obtenir les n plus grands éléments d'un tableau en JavaScript

Pour pratiquer la programmation en JavaScript, ouvrez le Terminal/SSH et tapez `node`. Une fois que vous avez fait cela, vous pouvez utiliser les étapes suivantes pour obtenir les `n` plus grands éléments d'un tableau :

1. Utilisez `Array.prototype.sort()` avec l'opérateur de propagation (`...`) pour créer un clone superficiel du tableau et le trier par ordre décroissant.
2. Utilisez `Array.prototype.slice()` pour obtenir le nombre spécifié d'éléments.
3. Si vous omettez le second argument, `n`, vous obtiendrez un tableau à un élément par défaut.
4. Si `n` est supérieur ou égal à la longueur du tableau fourni, renvoyez le tableau original (trié par ordre décroissant).

Voici le code JavaScript pour la fonction `maxN` qui implémente ces étapes :

```js
const maxN = (arr, n = 1) => [...arr].sort((a, b) => b - a).slice(0, n);
```

Vous pouvez tester la fonction `maxN` avec les exemples suivants :

```js
maxN([1, 2, 3]); // [3]
maxN([1, 2, 3], 2); // [3, 2]
```
