# Comment compter les sous-chaînes dans une chaîne de caractères à l'aide de JavaScript

Si vous voulez pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Cette fonction JavaScript compte le nombre d'occurrences d'une sous-chaîne spécifiée dans une chaîne de caractères donnée.

Pour utiliser cette fonction, suivez ces étapes :

1. Décarez une fonction appelée `countSubstrings` qui prend deux paramètres : `str` et `searchValue`.
2. Initialisez deux variables : `count` et `i`.
3. Utilisez la méthode `Array.prototype.indexOf()` pour rechercher `searchValue` dans `str`.
4. Si la valeur est trouvée, incrémentez la variable `count` et mettez à jour la variable `i`.
5. Utilisez une boucle `while` qui retourne dès que la valeur renvoyée par `Array.prototype.indexOf()` est `-1`.
6. Retournez la variable `count`.

Voici le code pour la fonction `countSubstrings` :

```js
const countSubstrings = (str, searchValue) => {
  let count = 0,
    i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) [count, i] = [count + 1, r + 1];
    else return count;
  }
};
```

Vous pouvez tester la fonction à l'aide des exemples ci-dessous :

```js
countSubstrings("tiktok tok tok tik tok tik", "tik"); // 3
countSubstrings("tutut tut tut", "tut"); // 4
```
