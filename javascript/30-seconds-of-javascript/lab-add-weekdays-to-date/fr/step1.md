# Fonction pour ajouter des jours ouvrables à une date donnée

Pour calculer une date future en ajoutant un nombre donné de jours ouvrables, vous pouvez utiliser la fonction `addWeekDays`. Voici les étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la fonction `addWeekDays` qui prend deux arguments : `startDate` et `count`.
3. `startDate` est la date à partir de laquelle vous voulez commencer à ajouter des jours ouvrables.
4. `count` est le nombre de jours ouvrables que vous voulez ajouter à la date de départ.
5. La fonction construit un tableau en utilisant la méthode `Array.from()` et définit la longueur égale au `count` de jours ouvrables à ajouter.
6. La méthode `Array.prototype.reduce()` est utilisée pour itérer sur le tableau, en commençant par `startDate`, et l'incrémenter en utilisant `Date.prototype.getDate()` et `Date.prototype.setDate()`.
7. La fonction vérifie si la `date` actuelle est un week-end ou non.
8. Si la `date` actuelle est un week-end, la fonction la met à jour en ajoutant un jour ou deux jours pour la rendre un jour ouvrable.
9. La fonction ne prend pas en compte les jours fériés officiels.

```js
const addWeekDays = (startDate, count) =>
  Array.from({ length: count }).reduce((date) => {
    date = new Date(date.setDate(date.getDate() + 1));
    if (date.getDay() % 6 === 0)
      date = new Date(date.setDate(date.getDate() + (date.getDay() / 6 + 1)));
    return date;
  }, startDate);
```

Voici quelques exemples de manière dont vous pouvez utiliser la fonction `addWeekDays` :

```js
addWeekDays(new Date("Oct 09, 2020"), 5); // 'Oct 16, 2020'
addWeekDays(new Date("Oct 12, 2020"), 5); // 'Oct 19, 2020'
```
