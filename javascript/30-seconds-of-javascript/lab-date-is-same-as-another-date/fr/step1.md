# Vérifier si deux dates sont identiques

Pour vérifier si deux dates sont identiques, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Date.prototype.toISOString()` et la vérification d'égalité stricte (`===`) pour comparer les deux dates.
3. Voici un extrait de code d'exemple :

```js
const isSameDate = (dateA, dateB) =>
  dateA.toISOString() === dateB.toISOString();
```

4. Testez la fonction avec deux dates en tant qu'arguments pour voir si elles sont identiques :

```js
isSameDate(new Date(2010, 10, 20), new Date(2010, 10, 20)); // true
```

Cette fonction vérifie si les deux dates sont identiques en comparant leurs représentations sous forme de chaîne ISO.
