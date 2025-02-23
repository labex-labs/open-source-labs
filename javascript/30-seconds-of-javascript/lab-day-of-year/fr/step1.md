# Comment obtenir le jour de l'année en JavaScript en utilisant l'objet Date

Pour obtenir le jour de l'année (nombre compris entre 1 et 366) à partir d'un objet `Date` en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez le constructeur `Date` et `Date.prototype.getFullYear()` pour obtenir le premier jour de l'année sous forme d'un objet `Date`.
3. Soustrayez le premier jour de l'année de l'objet `date` et divisez par le nombre de millisecondes dans chaque jour pour obtenir le résultat.
4. Utilisez `Math.floor()` pour arrondir le nombre de jours obtenu à un entier.

Voici le code :

```js
const dayOfYear = (date) =>
  Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
```

Pour tester la fonction, appelez `dayOfYear()` avec un objet `Date` en argument :

```js
dayOfYear(new Date()); // 272
```
