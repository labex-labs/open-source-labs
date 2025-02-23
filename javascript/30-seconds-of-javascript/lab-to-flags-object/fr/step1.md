# Conversion d'un tableau en objet de drapeaux

Si vous voulez commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

La fonction suivante convertit un tableau de chaînes de caractères en un objet qui est égal à `true`.

Pour ce faire, nous utilisons `Array.prototype.reduce()`. Cette méthode convertit le tableau en un objet, où chaque valeur du tableau sert de clé dont la valeur est définie sur `true`.

```js
const flags = (arr) => arr.reduce((acc, str) => ({ ...acc, [str]: true }), {});
```

Voici un exemple :

```js
flags(["red", "green"]); // { red: true, green: true }
```
