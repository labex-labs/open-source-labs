# Explications sur l'itérateur plat

Pour créer un générateur qui itère sur un itérable et aplatit les itérables imbriqués, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la récursivité dans la fonction génératrice.
3. Utilisez une boucle `for...of` pour itérer sur les valeurs de l'itérateur donné.
4. Utilisez `Symbol.iterator` pour vérifier si chaque valeur est un itérable.
5. Si c'est le cas, utilisez l'expression `yield*` pour déléguer de manière récursive à la même fonction génératrice.
6. Sinon, `yield` la valeur actuelle.

Voici un extrait de code d'exemple :

```js
const flatIterator = function* (itr) {
  for (let item of itr) {
    if (item[Symbol.iterator]) yield* flatIterator(item);
    else yield item;
  }
};

const arr = [1, 2, [3, 4], [5, [6, [7], 8]], 9, new Set([10, 11])];
[...flatIterator(arr)]; // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
```

Dans l'exemple, `arr` est un tableau de valeurs, y compris des tableaux imbriqués et un ensemble. La fonction génératrice `flatIterator` est utilisée pour aplatir ces valeurs imbriquées et renvoyer un tableau aplati.
