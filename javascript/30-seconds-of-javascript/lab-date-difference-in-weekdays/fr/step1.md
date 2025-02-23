# Compter les jours ouvrables entre deux dates

Pour compter les jours ouvrables entre deux dates, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.from()` pour créer un tableau avec une longueur égale au nombre de jours entre `startDate` et `endDate`.
3. Utilisez `Array.prototype.reduce()` pour itérer sur le tableau, vérifier si chaque date est un jour ouvrable et incrémenter `count`.
4. Mettez à jour `startDate` avec le lendemain à chaque itération en utilisant `Date.prototype.getDate()` et `Date.prototype.setDate()` pour l'avancer d'un jour.
5. Notez que cette fonction ne prend pas en compte les jours fériés officiels.

Voici le code pour implémenter cela :

```js
const countWeekDaysBetween = (startDate, endDate) =>
  Array.from({ length: (endDate - startDate) / (1000 * 3600 * 24) }).reduce(
    (count) => {
      if (startDate.getDay() % 6 !== 0) count++;
      startDate = new Date(startDate.setDate(startDate.getDate() + 1));
      return count;
    },
    0
  );
```

Vous pouvez utiliser le code suivant pour tester la fonction :

```js
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 06, 2020")); // 1
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 14, 2020")); // 7
```
