# Classement de tableaux

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Cette fonction calcule le classement d'un tableau en fonction d'une fonction de comparaison.

Pour utiliser cette fonction, vous pouvez :

- Utiliser `Array.prototype.map()` et `Array.prototype.filter()` pour mapper chaque élément à un classement en utilisant la fonction de comparaison fournie.

Voici un exemple d'utilisation :

```js
const ranking = (arr, compFn) =>
  arr.map((a) => arr.filter((b) => compFn(a, b)).length + 1);
```

Exemple :

```js
ranking([8, 6, 9, 5], (a, b) => a < b);
// [2, 3, 1, 4]
ranking(["c", "a", "b", "d"], (a, b) => a.localeCompare(b) > 0);
// [3, 1, 2, 4]
```
