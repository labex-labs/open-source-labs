# Comment vérifier si deux tableaux ont un élément commun

Pour vérifier si deux tableaux ont un élément commun, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Créez un `Set` à partir de `b` pour obtenir les valeurs uniques de `b`.
3. Utilisez `Array.prototype.some()` sur `a` pour vérifier si l'une de ses valeurs est contenue dans `b`, en utilisant `Set.prototype.has()`.
4. Utilisez la fonction `intersects` fournie ci-dessous pour tester les tableaux.

```js
const intersects = (a, b) => {
  const s = new Set(b);
  return [...new Set(a)].some((x) => s.has(x));
};
```

Utilisez la fonction `intersects` pour vérifier si deux tableaux se croisent :

```js
intersects(["a", "b"], ["b", "c"]); // true
intersects(["a", "b"], ["c", "d"]); // false
```

En suivant ces étapes et en utilisant le code fourni, vous pouvez facilement vérifier si deux tableaux ont un élément commun.
