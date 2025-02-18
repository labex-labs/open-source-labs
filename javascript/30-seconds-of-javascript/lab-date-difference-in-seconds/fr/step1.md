# Fonction pour calculer la différence entre deux dates en secondes

Pour calculer la différence entre deux dates en secondes, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Soustrayez les deux objets `Date` et divisez le résultat par le nombre de millisecondes dans une seconde.
3. Le résultat sera la différence entre les deux dates en secondes.

Voici une fonction JavaScript qui effectue ce calcul :

```js
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

Pour utiliser cette fonction, passez deux objets `Date` en tant qu'arguments, comme ceci :

```js
getSecondsDiffBetweenDates(
  new Date("2020-12-24 00:00:15"),
  new Date("2020-12-24 00:00:17")
); // 2
```
