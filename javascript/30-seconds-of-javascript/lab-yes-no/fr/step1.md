# Fonction pour vérifier une chaîne "oui"/"non"

Pour vérifier si une chaîne de caractères est une réponse "oui" ou "non", utilisez la fonction suivante dans le Terminal/SSH en tapant `node` :

```js
const yesNo = (val, def = false) =>
  /^(y|yes)$/i.test(val) ? true : /^(n|no)$/i.test(val) ? false : def;
```

- La fonction renvoie `true` si la chaîne est "y"/"yes" et `false` si la chaîne est "n"/"no".
- Pour définir une réponse par défaut, omettez le deuxième argument `def`. Par défaut, la fonction renverra `false`.
- La fonction utilise `RegExp.prototype.test()` pour vérifier si la chaîne correspond à "y"/"yes" ou "n"/"no".

Exemple d'utilisation :

```js
yesNo("Y"); // true
yesNo("yes"); // true
yesNo("No"); // false
yesNo("Foo", true); // true
```
