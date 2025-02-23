# Fonction pour renvoyer les n éléments les plus petits d'un tableau

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Utilisez la fonction `minN` pour renvoyer les `n` éléments les plus petits d'un tableau.

Voici comment utiliser la fonction :

- Utilisez `Array.prototype.sort()` et l'opérateur de propagation (`...`) pour créer un clone superficiel du tableau et le trier par ordre croissant.
- Utilisez `Array.prototype.slice()` pour obtenir le nombre spécifié d'éléments.
- Si vous omettez le second argument, `n`, la fonction renverra un tableau à un élément.
- Si `n` est supérieur ou égal à la longueur du tableau fourni, la fonction renverra le tableau original, trié par ordre croissant.

```js
const minN = (arr, n = 1) => [...arr].sort((a, b) => a - b).slice(0, n);
```

Voici quelques exemples :

```js
minN([1, 2, 3]); // [1]
minN([1, 2, 3], 2); // [1, 2]
```
