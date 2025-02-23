# Comment convertir un nombre au format avec la virgule décimale

Pour convertir un nombre au format avec la virgule décimale, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Number.prototype.toLocaleString()` pour convertir le nombre au format avec la virgule décimale.
3. Le code suivant peut être utilisé pour ce processus :

```js
const toDecimalMark = (num) => num.toLocaleString("en-US");
```

Voici un exemple d'utilisation de cette fonction :

```js
toDecimalMark(12305030388.9087); // '12,305,030,388.909'
```

Cela convertira le nombre `12305030388.9087` en la chaîne de caractères formatée avec la virgule décimale `'12,305,030,388.909'`.
