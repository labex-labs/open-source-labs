# Vérifier si une chaîne est au format ISO

Pour vérifier si une chaîne de caractères donnée est au format ISO étendu simplifié (ISO 8601), suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez le constructeur `Date` pour créer un objet `Date` à partir de la chaîne donnée.
3. Vérifiez si l'objet date produit est valide en utilisant `Date.prototype.valueOf()` et `Number.isNaN()`.
4. Comparez la représentation sous forme de chaîne au format ISO de la date avec la chaîne originale en utilisant `Date.prototype.toISOString()`.
5. Si les chaînes correspondent et que la date est valide, retournez `true`. Sinon, retournez `false`.

Voici un exemple de code :

```js
const isISOString = (val) => {
  const d = new Date(val);
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

isISOString("2020-10-12T10:10:10.000Z"); // true
isISOString("2020-10-12"); // false
```

Cette fonction retournera `true` si la chaîne est au format ISO, et `false` sinon.
