# Générateur qui produit des valeurs tant qu'une condition est vraie

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`. Cela créera un générateur qui continue de produire de nouvelles valeurs tant que la condition donnée est satisfaite.

Le générateur est initialisé avec une valeur `seed`, qui est utilisée pour initialiser la valeur `val` actuelle. Une boucle `while` est ensuite utilisée pour itérer tant que la fonction `condition` appelée avec la valeur `val` actuelle renvoie `true`.

Le mot clé `yield` est utilisé pour renvoyer la valeur `val` actuelle et éventuellement recevoir une nouvelle valeur `nextSeed`. La fonction `next` est utilisée pour calculer la valeur suivante à partir de la valeur `val` actuelle et de la valeur `nextSeed`.

```js
const generateWhile = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

Pour utiliser le générateur, appelez-le avec les fonctions `seed`, `condition` et `next`. Par exemple, l'appel `[...generateWhile(1, v => v <= 5, v => ++v)]` renverra `[1, 2, 3, 4, 5]`.
