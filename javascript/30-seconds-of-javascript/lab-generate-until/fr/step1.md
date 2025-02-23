# Générer des valeurs jusqu'à ce qu'une condition donnée soit remplie

Pour commencer à pratiquer le codage, ouvrez le Terminal/SSH et tapez `node`. Une fois que vous avez fait cela, vous pouvez créer un générateur qui produit de nouvelles valeurs jusqu'à ce qu'une condition donnée soit remplie.

Pour créer ce générateur, suivez ces étapes :

- Initialisez la valeur actuelle `val` à l'aide de la valeur `seed`.
- Utilisez une boucle `while` pour continuer à itérer tant que la fonction `condition`, appelée avec la valeur actuelle `val`, renvoie `false`.
- Utilisez le mot-clé `yield` pour renvoyer la valeur actuelle `val` et, facultativement, recevoir une nouvelle valeur de graine, `nextSeed`.
- Utilisez la fonction `next` pour calculer la valeur suivante à partir de la valeur actuelle `val` et de la `nextSeed`.

Voici un extrait de code d'exemple :

```js
const generateUntil = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (!condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

Vous pouvez utiliser le générateur en l'appelant avec les arguments appropriés. Par exemple :

```js
[
  ...generateUntil(
    1,
    (v) => v > 5,
    (v) => ++v
  )
]; // [1, 2, 3, 4, 5]
```

Cela produira un tableau de valeurs de `1` à `5`, car la condition `v > 5` est remplie lorsque `val` est égal à `6`.
