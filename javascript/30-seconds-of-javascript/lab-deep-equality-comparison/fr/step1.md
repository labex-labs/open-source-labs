# Comment vérifier l'égalité d'objets en JavaScript

Pour vérifier si deux valeurs sont équivalentes, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Effectuez une comparaison approfondie entre les deux valeurs en utilisant la fonction `equals()`.
3. Vérifiez si les deux valeurs sont identiques. Si c'est le cas, renvoyez `true`.
4. Vérifiez si les deux valeurs sont des objets `Date` avec la même heure, en utilisant `Date.prototype.getTime()`. Si c'est le cas, renvoyez `true`.
5. Vérifiez si les deux valeurs sont des valeurs non-objets avec une valeur équivalente (comparaison stricte). Si c'est le cas, renvoyez `true`.
6. Vérifiez si seule une des valeurs est `null` ou `undefined` ou si leurs prototypes diffèrent. Si c'est le cas, renvoyez `false`.
7. Si aucune des conditions ci-dessus n'est remplie, utilisez `Object.keys()` pour vérifier si les deux valeurs ont le même nombre de clés.
8. Utilisez `Array.prototype.every()` pour vérifier si chaque clé dans `a` existe dans `b` et si elles sont équivalentes en appelant `equals()` de manière récursive.

Utilisez le code suivant pour implémenter la fonction `equals()` :

```js
const equals = (a, b) => {
  if (a === b) return true;

  if (a instanceof Date && b instanceof Date)
    return a.getTime() === b.getTime();

  if (!a || !b || (typeof a !== "object" && typeof b !== "object"))
    return a === b;

  if (a.prototype !== b.prototype) return false;

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every((k) => equals(a[k], b[k]));
};
```

Utilisez les exemples de code suivants pour tester la fonction `equals()` :

```js
equals(
  { a: [2, { e: 3 }], b: [4], c: "foo" },
  { a: [2, { e: 3 }], b: [4], c: "foo" }
); // true

equals([1, 2, 3], { 0: 1, 1: 2, 2: 3 }); // true
```
