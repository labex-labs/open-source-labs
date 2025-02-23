# Vérification d'itérateurs disjoints

Pour vérifier si deux itérateurs n'ont pas de valeurs communes, vous pouvez utiliser la fonction `isDisjoint`.

Voici comment l'utiliser :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Créez un nouvel objet `Set` à partir de chaque itérateur en utilisant le constructeur `Set`.
3. Utilisez `Array.prototype.every()` et `Set.prototype.has()` pour vérifier que les deux itérateurs n'ont pas de valeurs communes.

```js
const isDisjoint = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sA].every((v) => !sB.has(v));
};
```

Voici quelques exemples :

```js
isDisjoint(new Set([1, 2]), new Set([3, 4])); // true
isDisjoint(new Set([1, 2]), new Set([1, 3])); // false
```
