# Voici comment obtenir l'heure au format avec deux points à partir d'un objet de date

Si vous cherchez à pratiquer la programmation, vous pouvez commencer par ouvrir le Terminal/SSH et en tapant `node`.

Cette fonction renvoie une chaîne de caractères au format `HH:MM:SS` à partir d'un objet `Date` donné.

Pour y arriver, les méthodes `Date.prototype.toTimeString()` et `String.prototype.slice()` sont utilisées pour extraire la partie `HH:MM:SS` de l'objet `Date`.

Voici le code de la fonction :

```js
const getColonTimeFromDate = (date) => date.toTimeString().slice(0, 8);
```

Et voici un exemple d'utilisation :

```js
getColonTimeFromDate(new Date()); // '08:38:00'
```
