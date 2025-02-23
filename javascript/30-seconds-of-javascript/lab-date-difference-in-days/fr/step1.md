# Fonction pour calculer la différence de dates en jours

Pour calculer la différence entre deux dates en jours, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la fonction `getDaysDiffBetweenDates` avec deux objets `Date` en arguments.
3. La fonction soustraira la date initiale de la date finale et divisera le résultat par le nombre de millisecondes dans une journée pour obtenir la différence en jours entre elles.

Voici le code de la fonction `getDaysDiffBetweenDates` :

```js
const getDaysDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600 * 24);
```

Pour utiliser la fonction, passez deux objets `Date` au format `AAAA-MM-JJ` :

```js
getDaysDiffBetweenDates(new Date("2017-12-13"), new Date("2017-12-22")); // 9
```

Cela renverra la différence entre les deux dates en jours, qui est 9 dans cet exemple.
