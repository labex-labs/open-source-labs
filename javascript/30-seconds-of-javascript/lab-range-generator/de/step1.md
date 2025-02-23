# Bereichsgenerator

Um einen Bereich von Werten mit einem angegebenen Schritt zu erzeugen, verwenden Sie die folgende `rangeGenerator`-Funktion. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen zu codieren.

- Verwenden Sie eine `while`-Schleife und `yield`, um jeden Wert zurückzugeben, beginnend bei `start` und endend bei `end`.
- Wenn Sie einen Standardschritt von `1` verwenden möchten, lassen Sie das dritte Argument weg.

```js
const rangeGenerator = function* (start, end, step = 1) {
  let i = start;
  while (i < end) {
    yield i;
    i += step;
  }
};
```

Hier ist ein Beispiel dafür, wie die `rangeGenerator`-Funktion verwendet wird:

```js
for (let i of rangeGenerator(6, 10)) console.log(i);
// Gibt 6, 7, 8, 9 aus
```
