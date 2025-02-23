# Comment calculer la médiane d'un tableau de nombres

Pour calculer la médiane d'un tableau de nombres, suivez ces étapes :

1. Trouvez le milieu du tableau.
2. Utilisez `Array.prototype.sort()` pour trier les valeurs.
3. Si `Array.prototype.length` est impair, renvoyez le nombre au point médian. Si c'est pair, renvoyez la moyenne des deux nombres du milieu.
4. Pour commencer à pratiquer la programmation et à utiliser `node`, ouvrez le Terminal/SSH et tapez `node`.

Voici un extrait de code d'exemple qui implémente cette logique :

```js
const median = (arr) => {
  const mid = Math.floor(arr.length / 2),
    nums = [...arr].sort((a, b) => a - b);
  return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};
```

Vous pouvez appeler cette fonction avec un tableau de nombres comme indiqué ci-dessous :

```js
median([5, 6, 50, 1, -5]); // 5
```
