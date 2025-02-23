# Fonction JavaScript pour Calculer la Différence de Dates en Heures

Pour calculer la différence entre deux dates en heures à l'aide de JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Utilisez la fonction JavaScript suivante pour obtenir la différence (en heures) entre deux objets `Date` :

```js
const getHoursDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600);
```

3. Appelez la fonction avec les deux dates en tant qu'arguments pour obtenir la différence en heures :

```js
getHoursDiffBetweenDates(
  new Date("2021-04-24 10:25:00"),
  new Date("2021-04-25 10:25:00")
); // 24
```
