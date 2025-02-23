# Index of Substrings

Pour trouver tous les index d'une sous-chaîne dans une chaîne donnée, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode intégrée `Array.prototype.indexOf()` pour rechercher `searchValue` dans `str`.
3. Utilisez `yield` pour renvoyer l'index si la valeur est trouvée et mettre à jour l'index, `i`.
4. Utilisez une boucle `while` qui terminera le générateur dès que la valeur renvoyée par `Array.prototype.indexOf()` est `-1`.

Voici un exemple de code pour implémenter les étapes ci-dessus :

```js
const indexOfSubstrings = function* (str, searchValue) {
  let i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) {
      yield r;
      i = r + 1;
    } else return;
  }
};
```

Vous pouvez tester la fonction avec le code suivant :

```js
[...indexOfSubstrings("tiktok tok tok tik tok tik", "tik")]; // [0, 15, 23]
[...indexOfSubstrings("tutut tut tut", "tut")]; // [0, 2, 6, 10]
[...indexOfSubstrings("hello", "hi")]; // []
```
