# Fonction pour vérifier si une chaîne est alphabétique

Pour vérifier si une chaîne de caractères ne contient que des caractères alphabétiques :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez `RegExp.prototype.test()` pour vérifier si la chaîne donnée correspond au motif d'expression régulière alphabétique.
- La fonction `isAlpha` prend une chaîne en argument et renvoie `true` si la chaîne ne contient que des caractères alphabétiques, et `false` sinon.

Voici un exemple :

```js
const isAlpha = (str) => /^[a-zA-Z]*$/.test(str);
```

```js
isAlpha("sampleInput"); // true
isAlpha("this Will fail"); // false
isAlpha("123"); // false
```
