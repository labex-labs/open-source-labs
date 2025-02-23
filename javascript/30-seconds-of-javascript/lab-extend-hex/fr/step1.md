# Comment étendre un code couleur à 3 chiffres en un code couleur à 6 chiffres

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Vous pouvez utiliser la fonction suivante pour étendre un code couleur à 3 chiffres en un code couleur à 6 chiffres :

```js
const extendHex = (shortHex) =>
  "#" +
  shortHex
    .slice(shortHex.startsWith("#") ? 1 : 0)
    .split("")
    .map((x) => x + x)
    .join("");
```

Pour convertir un code hexadécimal de couleur RGB noté sur 3 chiffres en la forme sur 6 chiffres, suivez ces étapes :

- Utilisez `Array.prototype.map()`, `String.prototype.split()` et `Array.prototype.join()` pour joindre le tableau mappé.
- Utilisez `Array.prototype.slice()` pour supprimer le `#` du début de la chaîne car il est ajouté une fois.

Voici quelques exemples :

```js
extendHex("#03f"); // '#0033ff'
extendHex("05a"); // '#0055aa'
```
