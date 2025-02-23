# Fonction pour calculer la différence entre deux dates en minutes

Pour calculer la différence (en minutes) entre deux dates, utilisez la fonction suivante :

```js
const getMinutesDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 60);
```

Il suffit de soustraire les deux objets `Date` et de diviser par le nombre de millisecondes dans une minute pour obtenir la différence (en minutes) entre eux.

Voici un exemple d'utilisation de la fonction :

```js
getMinutesDiffBetweenDates(
  new Date("2021-04-24 01:00:15"),
  new Date("2021-04-24 02:00:15")
); // 60
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
