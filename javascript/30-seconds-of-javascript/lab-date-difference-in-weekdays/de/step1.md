# Zähle die Werktage zwischen zwei Daten

Um die Werktage zwischen zwei Daten zu zählen, folge diesen Schritten:

1. Öffne das Terminal/SSH und tippe `node`, um mit der Code-Praxis zu beginnen.
2. Verwende `Array.from()`, um ein Array zu erstellen, dessen Länge der Anzahl der Tage zwischen `startDate` und `endDate` entspricht.
3. Verwende `Array.prototype.reduce()`, um über das Array zu iterieren, überprüfe, ob jedes Datum ein Werktag ist und erhöhe `count`.
4. Aktualisiere `startDate` mit dem nächsten Tag in jeder Schleife, indem du `Date.prototype.getDate()` und `Date.prototype.setDate()` verwendest, um es um einen Tag voranzuschieben.
5. Beachte, dass diese Funktion keine offiziellen Feiertage berücksichtigt.

Hier ist der Code, um dies umzusetzen:

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

Du kannst folgenden Code verwenden, um die Funktion zu testen:

```js
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 06, 2020")); // 1
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 14, 2020")); // 7
```
