# Fonction pour Vérifier si Un Ensemble est un Surensemble d'un Autre Ensemble

Pour vérifier si un ensemble est un surensemble d'un autre ensemble, utilisez la fonction `superSet()`. Tout d'abord, ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation. Ensuite, suivez les étapes suivantes :

- Créez un nouvel objet `Set` à partir de chaque itérable en utilisant le constructeur `Set`.
- Utilisez `Array.prototype.every()` et `Set.prototype.has()` pour vérifier que chaque valeur de la seconde itérable est contenue dans la première.
- La fonction renvoie `true` si la première itérable est un surensemble de la seconde, en excluant les valeurs dupliquées. Sinon, elle renvoie `false`.

```js
const superSet = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sB].every((v) => sA.has(v));
};
```

Utilisez `superSet()` avec deux ensembles en arguments pour vérifier si un ensemble est un surensemble de l'autre.

```js
superSet(new Set([1, 2, 3, 4]), new Set([1, 2])); // true
superSet(new Set([1, 2, 3, 4]), new Set([1, 5])); // false
```
