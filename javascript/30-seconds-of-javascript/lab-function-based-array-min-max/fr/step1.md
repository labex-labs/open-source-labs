# Comment trouver le minimum et le maximum d'un tableau à l'aide d'une fonction fournie

Pour pratiquer la programmation, ouvrez le Terminal ou SSH et tapez `node`.

Voici une fonction qui renvoie les valeurs minimales et maximales d'un tableau, en fonction d'une fonction fournie qui définit la règle de comparaison :

```js
const reduceWhich = (arr, comparator = (a, b) => a - b) =>
  arr.reduce((a, b) => (comparator(a, b) >= 0 ? b : a));
```

Pour l'utiliser, suivez ces étapes :

1. Appelez `reduceWhich` avec le tableau que vous voulez traiter et la fonction `comparator` optionnelle.
2. La fonction `reduceWhich` utilisera `Array.prototype.reduce()` en combinaison avec la fonction `comparator` pour retourner l'élément approprié dans le tableau.
3. Si vous omettez le second argument (`comparator`), la fonction par défaut sera utilisée, qui renvoie l'élément minimum du tableau.

Voici quelques exemples d'utilisation de `reduceWhich` :

```js
reduceWhich([1, 3, 2]); // 1
reduceWhich([1, 3, 2], (a, b) => b - a); // 3
reduceWhich(
  [
    { name: "Tom", age: 12 },
    { name: "Jack", age: 18 },
    { name: "Lucy", age: 9 }
  ],
  (a, b) => a.age - b.age
); // {name: 'Lucy', age: 9}
```

Dans les exemples ci-dessus, le premier appel à `reduceWhich` renvoie la valeur minimale du tableau `[1, 3, 2]`, qui est `1`. Le second appel renvoie la valeur maximale du même tableau, en fonction de la fonction `comparator` qui inverse l'ordre de comparaison. Le troisième appel renvoie l'objet dans le tableau qui a la propriété `age` minimale, en fonction de la fonction `comparator` qui compare les propriétés `age` des objets.
