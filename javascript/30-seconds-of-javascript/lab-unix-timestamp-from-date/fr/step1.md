# Comment obtenir le timestamp Unix à partir d'une date en JavaScript

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

Vous pouvez utiliser les étapes suivantes pour obtenir le timestamp Unix à partir d'un objet `Date` en JavaScript :

1. Utilisez `Date.prototype.getTime()` pour obtenir le timestamp en millisecondes.
2. Divisez le timestamp par `1000` pour obtenir le timestamp en secondes.
3. Utilisez `Math.floor()` pour arrondir le timestamp résultant à un entier.
4. Si vous omettez l'argument `date`, la date actuelle sera utilisée.

Voici un extrait de code exemple :

```js
const getTimestamp = (date = new Date()) => Math.floor(date.getTime() / 1000);
```

Vous pouvez appeler la fonction `getTimestamp()` pour obtenir le timestamp Unix. Par exemple :

```js
getTimestamp(); // 1602162242
```
