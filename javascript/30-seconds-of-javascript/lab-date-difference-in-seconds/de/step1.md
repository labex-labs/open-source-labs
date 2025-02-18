# Funktion zur Berechnung der Datumsdifferenz in Sekunden

Um die Differenz zwischen zwei Daten in Sekunden zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.
2. Subtrahieren Sie die beiden `Date`-Objekte und teilen Sie das Ergebnis durch die Anzahl der Millisekunden in einer Sekunde.
3. Das Ergebnis ist die Differenz zwischen den beiden Daten in Sekunden.

Hier ist eine JavaScript-Funktion, die diese Berechnung durchführt:

```js
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

Um diese Funktion zu verwenden, übergeben Sie zwei `Date`-Objekte als Argumente, wie hier:

```js
getSecondsDiffBetweenDates(
  new Date("2020-12-24 00:00:15"),
  new Date("2020-12-24 00:00:17")
); // 2
```
