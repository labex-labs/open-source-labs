# Fonction pour calculer la différence de dates en mois

Pour calculer la différence entre deux dates en mois, utilisez la fonction suivante :

```js
const getMonthsDiffBetweenDates = (dateInitial, dateFinal) =>
  Math.max(
    (dateFinal.getFullYear() - dateInitial.getFullYear()) * 12 +
      dateFinal.getMonth() -
      dateInitial.getMonth(),
    0
  );
```

Pour utiliser cette fonction, passez deux objets `Date` en tant qu'arguments. Par exemple :

```js
getMonthsDiffBetweenDates(new Date("2017-12-13"), new Date("2018-04-29")); // 4
```

Cette fonction utilise les méthodes `Date.prototype.getFullYear()` et `Date.prototype.getMonth()` pour calculer la différence en mois entre deux dates.
