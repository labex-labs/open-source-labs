# Funktion zum Berechnen des Datumsunterschieds in Tagen

Um den Unterschied zwischen zwei Daten in Tagen zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die Funktion `getDaysDiffBetweenDates` mit zwei `Date`-Objekten als Argumenten.
3. Die Funktion wird das Anfangsdatum von dem Enddatum subtrahieren und das Ergebnis durch die Anzahl der Millisekunden in einem Tag dividieren, um den Unterschied in Tagen zwischen ihnen zu erhalten.

Hier ist der Code für die Funktion `getDaysDiffBetweenDates`:

```js
const getDaysDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600 * 24);
```

Um die Funktion zu verwenden, übergeben Sie zwei `Date`-Objekte im Format `YYYY-MM-DD`:

```js
getDaysDiffBetweenDates(new Date("2017-12-13"), new Date("2017-12-22")); // 9
```

Dies wird den Unterschied zwischen den beiden Daten in Tagen zurückgeben, was in diesem Beispiel 9 ist.
