# Fonction pour Trouver les Valeurs Uniques Inversées dans un Tableau

Pour trouver toutes les valeurs uniques d'un tableau en fonction d'une fonction de comparaison fournie à partir de la droite, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduceRight()` et `Array.prototype.some()` pour créer un tableau ne contenant que la dernière occurrence unique de chaque valeur, en fonction de la fonction de comparaison `fn`.
3. La fonction de comparaison prend deux arguments : les valeurs des deux éléments en cours de comparaison.
4. Voici le code pour implémenter la fonction :

```js
const uniqueElementsByRight = (arr, fn) =>
  arr.reduceRight((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

5. Utilisez le code suivant pour tester la fonction :

```js
uniqueElementsByRight(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'e' }, { id: 1, value: 'd' }, { id: 2, value: 'c' } ]
```
