# Une fonction pour trouver la correspondance numérique la plus proche dans un tableau

Pour trouver le nombre le plus proche dans un tableau, utilisez la fonction suivante :

```js
const closest = (arr, n) =>
  arr.reduce((acc, num) => (Math.abs(num - n) < Math.abs(acc - n) ? num : acc));
```

Voici comment l'utiliser :

1. Ouvrez le Terminal/SSH.
2. Tapez `node`.
3. Utilisez la fonction `closest()` et fournissez le tableau et la valeur cible en tant qu'arguments.

Utilisation exemple : `closest([6, 1, 3, 7, 9], 5)` renverra `6`, qui est le nombre le plus proche de `5` dans le tableau.
