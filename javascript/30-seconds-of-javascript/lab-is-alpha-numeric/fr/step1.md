# Vérification si une chaîne est alphanumérique

Si vous souhaitez pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Voici une fonction qui vérifie si une chaîne de caractères ne contient que des caractères alphanumériques :

```js
const isAlphaNumeric = (str) => /^[a-z0-9]+$/gi.test(str);
```

Pour l'utiliser, appelez `isAlphaNumeric` en lui passant une chaîne de caractères comme argument. Elle renverra `true` si la chaîne ne contient que des caractères alphanumériques, et `false` sinon.

Par exemple :

```js
isAlphaNumeric("hello123"); // true
isAlphaNumeric("123"); // true
isAlphaNumeric("hello 123"); // false (contient un espace)
isAlphaNumeric("#$hello"); // false (contient des caractères non alphanumériques)
```

La méthode `RegExp.prototype.test()` est utilisée pour vérifier si la chaîne d'entrée correspond au motif alphanumérique, qui est représenté par l'expression régulière `/^[a-z0-9]+$/gi`. Ce motif correspond à toute séquence d'une ou plusieurs lettres minuscules ou de chiffres, et les indicateurs `g` et `i` rendent la correspondance insensible à la casse.
