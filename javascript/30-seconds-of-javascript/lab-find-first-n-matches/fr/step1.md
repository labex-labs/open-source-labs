# Comment Trouver les Premières N Correspondances

Pour trouver les premiers `n` éléments qui répondent à un certain critère, utilisez la fonction `findFirstN`. Voici comment :

1. Ouvrez le Terminal/SSH.
2. Tapez `node` pour commencer à pratiquer la programmation.
3. Utilisez la fonction `findFirstN`, en passant le tableau à parcourir, une fonction de correspondance et le nombre de correspondances à trouver (si non spécifié, la valeur par défaut est 1).
4. La fonction `matcher` sera exécutée pour chaque élément du `arr`, et si elle renvoie une valeur véridique, cet élément sera ajouté au tableau de résultats.
5. Si le tableau `res` atteint une longueur de `n`, la fonction renverra le tableau de résultats.
6. Si aucune correspondance n'est trouvée, un tableau vide sera renvoyé.

Voici le code de la fonction `findFirstN` :

```js
const findFirstN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i in arr) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.push(el);
    if (res.length === n) return res;
  }
  return res;
};
```

Et voici quelques exemples d'utilisation :

```js
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [2, 4]
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
