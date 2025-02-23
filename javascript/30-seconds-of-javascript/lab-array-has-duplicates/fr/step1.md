# Comment vérifier les doublons dans un tableau

Pour vérifier si un tableau contient des valeurs en double, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Set` pour obtenir les valeurs uniques dans le tableau.
3. Utilisez `Set.prototype.size` et `Array.prototype.length` pour vérifier si le nombre de valeurs uniques est le même que le nombre d'éléments dans le tableau original.

Voici un extrait de code d'exemple qui vérifie les doublons dans un tableau :

```js
const hasDuplicates = (arr) => new Set(arr).size !== arr.length;
```

Vous pouvez tester cette fonction avec le code suivant :

```js
hasDuplicates([0, 1, 1, 2]); // true
hasDuplicates([0, 1, 2, 3]); // false
```

La fonction `hasDuplicates` renvoie `true` s'il y a des valeurs en double dans le tableau, et `false` sinon.
