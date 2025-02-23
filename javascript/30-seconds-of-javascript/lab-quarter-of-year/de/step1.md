# Funktion zum Bestimmen des Jahresquartals

Um das Quartal des Jahres zu bestimmen, verwenden Sie die `quarterOfYear()`-Funktion. Diese Funktion nimmt einen optionalen `date`-Argument entgegen und gibt ein Array mit dem Quartal und dem Jahr zurück, zu dem das übergebene Datum gehört.

Um diese Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Kopieren und einfügen Sie dann folgenden Code:

```js
const quarterOfYear = (date = new Date()) => [
  Math.ceil((date.getMonth() + 1) / 3),
  date.getFullYear()
];
```

Die `quarterOfYear()`-Funktion verwendet die folgenden Schritte, um das Quartal und das Jahr zu berechnen:

- Verwenden Sie `Date.prototype.getMonth()`, um den aktuellen Monat im Bereich (0, 11) zu erhalten, und addieren Sie `1`, um ihn auf den Bereich (1, 12) abzubilden.
- Verwenden Sie `Math.ceil()` und teilen Sie den Monat durch `3`, um das aktuelle Quartal zu erhalten.
- Verwenden Sie `Date.prototype.getFullYear()`, um das Jahr aus dem angegebenen `date` zu erhalten.
- Lassen Sie das Argument `date` weg, um standardmäßig das aktuelle Datum zu verwenden.

Hier sind einige Beispiele für die Verwendung der `quarterOfYear()`-Funktion:

```js
quarterOfYear(new Date("07/10/2018")); // [ 3, 2018 ]
quarterOfYear(); // [ 4, 2020 ]
```
