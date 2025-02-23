# Instructions to find Last N Matches

Pour trouver les derniers `n` éléments qui correspondent à une certaine condition, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la fonction `findLastN` fournie ci-dessous.
3. Fournissez un tableau `arr` et une fonction `matcher` qui renvoie une valeur véridique pour les éléments que vous souhaitez correspondre.
4. Facultativement, vous pouvez également fournir le nombre `n` de correspondances que vous souhaitez renvoyer (la valeur par défaut est 1).
5. La fonction exécutera la fonction `matcher` pour chaque élément de `arr` à l'aide d'une boucle `for`, en commençant par le dernier élément.
6. Si un élément correspond à la condition `matcher`, il sera ajouté au tableau de résultats à l'aide de `Array.prototype.unshift()`, qui ajoute des éléments en tête du tableau.
7. Lorsque la longueur du tableau de résultats est égale à `n`, la fonction renverra les résultats.
8. Si il n'y a pas de correspondances ou si `n` est supérieur au nombre de correspondances, un tableau vide sera renvoyé.

```js
const findLastN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.unshift(el);
    if (res.length === n) return res;
  }
  return res;
};
```

Voici quelques exemples d'utilisation de la fonction `findLastN` :

```js
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [4, 6]
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
