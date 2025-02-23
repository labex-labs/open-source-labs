# Überprüfen, ob ein Datum zwischen zwei anderen Daten liegt

Um zu überprüfen, ob ein Datum zwischen zwei anderen Daten liegt, verwenden Sie in JavaScript die größer- als (`>`) und kleiner- als (`<`) Operatoren. Hier ist eine Beispiel-Funktion:

```js
const isBetweenDates = (dateStart, dateEnd, date) =>
  date > dateStart && date < dateEnd;
```

Um diese Funktion zu verwenden, übergeben Sie das Startdatum, das Enddatum und das zu überprüfende Datum. Die Funktion wird `true` zurückgeben, wenn das Datum zwischen dem Start- und Enddatum liegt, und `false` sonst. Hier sind einige Beispiele:

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

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
