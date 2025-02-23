# Funktion zur Berechnung des Zeitunterschieds in Minuten

Um den Zeitunterschied (in Minuten) zwischen zwei Daten zu berechnen, verwenden Sie die folgende Funktion:

```js
const getMinutesDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 60);
```

Subtrahieren Sie einfach die beiden `Date`-Objekte und dividieren Sie durch die Anzahl der Millisekunden in einer Minute, um den Zeitunterschied (in Minuten) zwischen ihnen zu erhalten.

Hier ist ein Beispiel für die Verwendung der Funktion:

```js
getMinutesDiffBetweenDates(
  new Date("2021-04-24 01:00:15"),
  new Date("2021-04-24 02:00:15")
); // 60
```

Um zu beginnen, mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
