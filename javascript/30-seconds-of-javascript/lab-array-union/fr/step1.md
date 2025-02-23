# Comment trouver l'union de deux tableaux en JavaScript

Pour trouver l'union de deux tableaux en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. L'union de deux tableaux renvoie chaque élément qui existe dans l'un ou l'autre des deux tableaux au moins une fois.

3. Pour obtenir l'union de deux tableaux, créez un `Set` avec toutes les valeurs de `a` et `b`, puis convertissez-le en tableau en utilisant la méthode `Array.from()`.

Voici un exemple de mise en œuvre :

```js
const union = (a, b) => Array.from(new Set([...a, ...b]));

console.log(union([1, 2, 3], [4, 3, 2])); // Sortie : [1, 2, 3, 4]
```

Dans l'exemple ci-dessus, la fonction `union()` prend deux tableaux, `[1, 2, 3]` et `[4, 3, 2]`, en arguments et renvoie l'union des deux tableaux sous forme d'un tableau `[1, 2, 3, 4]`.
