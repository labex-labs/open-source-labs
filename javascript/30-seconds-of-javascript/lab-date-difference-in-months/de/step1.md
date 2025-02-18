# Funktion zur Berechnung des Datumsunterschieds in Monaten

Um den Unterschied zwischen zwei Daten in Monaten zu berechnen, verwenden Sie die folgende Funktion:

```js
const getMonthsDiffBetweenDates = (dateInitial, dateFinal) =>
  Math.max(
    (dateFinal.getFullYear() - dateInitial.getFullYear()) * 12 +
      dateFinal.getMonth() -
      dateInitial.getMonth(),
    0
  );
```

Um diese Funktion zu verwenden, übergeben Sie zwei `Date`-Objekte als Argumente. Beispielsweise:

```js
getMonthsDiffBetweenDates(new Date("2017-12-13"), new Date("2018-04-29")); // 4
```

Diese Funktion verwendet die Methoden `Date.prototype.getFullYear()` und `Date.prototype.getMonth()`, um den Unterschied in Monaten zwischen zwei Daten zu berechnen.
