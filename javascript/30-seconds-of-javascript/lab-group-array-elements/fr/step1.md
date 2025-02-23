# Group Array Elements

Pour regrouper les éléments de tableaux en fonction de leur position dans les tableaux originaux, utilisez la fonction `zip` ci-dessous.

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- La fonction `zip` utilise `Math.max()` et `Function.prototype.apply()` pour obtenir le tableau le plus long parmi les arguments.
- Elle crée un tableau de cette longueur comme valeur de retour et utilise `Array.from()` avec une fonction de mapping pour créer un tableau d'éléments regroupés.
- Si les longueurs des tableaux d'arguments varient, `undefined` est utilisé là où aucune valeur n'a été trouvée.

```js
const zip = (...arrays) => {
  const maxLength = Math.max(...arrays.map((x) => x.length));
  return Array.from({ length: maxLength }).map((_, i) => {
    return Array.from({ length: arrays.length }, (_, k) => arrays[k][i]);
  });
};
```

Exemple d'utilisation :

```js
zip(["a", "b"], [1, 2], [true, false]); // [['a', 1, true], ['b', 2, false]]
zip(["a"], [1, 2], [true, false]); // [['a', 1, true], [undefined, 2, false]]
```
