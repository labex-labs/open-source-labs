# Wie man im JavaScript das Datum des Jahres mithilfe des Date-Objekts erhält

Um das Datum des Jahres (Zahl zwischen 1 und 366) aus einem `Date`-Objekt im JavaScript zu erhalten, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den `Date`-Konstruktor und `Date.prototype.getFullYear()`, um das erste Datum des Jahres als `Date`-Objekt zu erhalten.
3. Subtrahieren Sie das erste Datum des Jahres vom `date`-Objekt und dividieren Sie durch die Millisekunden pro Tag, um das Ergebnis zu erhalten.
4. Verwenden Sie `Math.floor()`, um die berechnete Tageszahl auf eine ganze Zahl zu runden.

Hier ist der Code:

```js
const dayOfYear = (date) =>
  Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
```

Um die Funktion zu testen, rufen Sie `dayOfYear()` mit einem `Date`-Objekt als Argument auf:

```js
dayOfYear(new Date()); // 272
```
