# Unfold Array

Pour créer un tableau à l'aide d'une fonction itératrice et d'une valeur initiale, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez une boucle `while` et `Array.prototype.push()` pour appeler la fonction itératrice plusieurs fois jusqu'à ce qu'elle retourne `false`.
3. La fonction itératrice devrait accepter un argument (`seed`) et toujours retourner un tableau avec deux éléments ([`value`, `nextSeed`]) ou `false` pour terminer.

Utilisez le code suivant pour implémenter la fonction `unfold` :

```js
const unfold = (fn, seed) => {
  let result = [],
    val = [null, seed];
  while ((val = fn(val[1]))) result.push(val[0]);
  return result;
};
```

Voici un exemple d'utilisation de la fonction `unfold` :

```js
var f = (n) => (n > 50 ? false : [-n, n + 10]);
unfold(f, 10); // [-10, -20, -30, -40, -50]
```

Cela produira un tableau avec des valeurs générées par la fonction itératrice `f` à partir de la valeur initiale de `10`. La fonction itératrice génère un tableau avec deux éléments à chaque étape : la négation de la valeur actuelle de la graine et la valeur de la graine suivante, qui est incrémentée de 10. Le processus continue jusqu'à ce que la valeur de la graine soit supérieure à 50, auquel moment la fonction retourne `false`.
