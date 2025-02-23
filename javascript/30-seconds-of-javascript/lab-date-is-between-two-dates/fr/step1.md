# Vérifier si une date se situe entre deux dates

Pour vérifier si une date se situe entre deux autres dates, utilisez les opérateurs supérieur (`>`) et inférieur (`<`) en JavaScript. Voici une fonction exemple :

```js
const isBetweenDates = (dateStart, dateEnd, date) =>
  date > dateStart && date < dateEnd;
```

Pour utiliser cette fonction, passez la date de début, la date de fin et la date à vérifier. La fonction renverra `true` si la date se situe entre la date de début et la date de fin, et `false` sinon. Voici quelques exemples :

```js
isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 19)
); // false

isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 25)
); // true
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
