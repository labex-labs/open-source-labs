# Ermitteln der Kalenderwoche aus einem Datum in JavaScript

Um die nullbasierte Kalenderwoche des Jahres zu ermitteln, die einem bestimmten Datum in JavaScript entspricht, befolgen Sie diese Schritte:

1. Erstellen Sie eine `weekOfYear`-Funktion, die einen `date`-Parameter akzeptiert.
2. Verwenden Sie den `Date`-Konstruktor und `Date.prototype.getFullYear()`, um den ersten Tag des Jahres als `Date`-Objekt zu erhalten.
3. Verwenden Sie `Date.prototype.setDate()`, `Date.prototype.getDate()` und `Date.prototype.getDay()` zusammen mit dem Modulo-Operator (`%`), um den ersten Montag des Jahres zu ermitteln.
4. Subtrahieren Sie den ersten Montag des Jahres vom angegebenen `date` und teilen Sie das Ergebnis durch die Anzahl der Millisekunden in einer Woche.
5. Verwenden Sie `Math.round()`, um die nullbasierte Kalenderwoche des Jahres zu erhalten, die dem angegebenen `date` entspricht.
6. Wenn das angegebene `date` vor dem ersten Montag des Jahres liegt, wird `-0` zurückgegeben.

Hier ist der Code:

```js
const weekOfYear = (date) => {
  const startOfYear = new Date(date.getFullYear(), 0, 1);
  startOfYear.setDate(startOfYear.getDate() + (startOfYear.getDay() % 7));
  return Math.round((date - startOfYear) / (7 * 24 * 3600 * 1000));
};
```

Um die `weekOfYear`-Funktion zu verwenden, rufen Sie sie einfach mit einem `Date`-Objekt als Parameter auf:

```js
weekOfYear(new Date("2021-06-18")); // 23
```

Dies wird die nullbasierte Kalenderwoche des Jahres zurückgeben, die dem angegebenen Datum entspricht, in diesem Fall `23`.
