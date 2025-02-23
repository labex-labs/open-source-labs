# Datumsbereichsgenerator

Um alle Datumsangaben in einem bestimmten Bereich mit einem angegebenen Schritt zu generieren, verwenden Sie folgenden Code in der Konsole/SSH und geben Sie `node` ein:

```js
const dateRangeGenerator = function* (start, end, step = 1) {
  let d = start;
  while (d < end) {
    yield new Date(d);
    d.setDate(d.getDate() + step);
  }
};
```

Dies erstellt einen Generator, der mithilfe einer `while`-Schleife von `start` bis `end` iteriert, den `Date`-Konstruktor verwendet, um jede Datumsangabe im Bereich zurückzugeben und um `step` Tage zu erhöhen, indem `Date.prototype.getDate()` und `Date.prototype.setDate()` verwendet werden.

Um einen Standardwert von `1` für `step` zu verwenden, lassen Sie das dritte Argument weg.

Hier ist ein Beispiel dafür, wie der `dateRangeGenerator` verwendet werden kann:

```js
[...dateRangeGenerator(new Date("2021-06-01"), new Date("2021-06-04"))];
// [ 2021-06-01, 2021-06-02, 2021-06-03 ]
```
