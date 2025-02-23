# Ein initialisiertes abgebildetes Array in JavaScript initialisieren

Um ein abgebildetes Array in JavaScript zu initialisieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den `Array()`-Konstruktor, um ein Array der gewünschten Länge zu erstellen.
3. Verwenden Sie `Array.prototype.fill()`, um das Array mit `null`-Werten zu füllen.
4. Verwenden Sie `Array.prototype.map()`, um das Array mit den gewünschten Werten zu füllen, indem Sie die bereitgestellte Funktion `mapFn` verwenden.
5. Überspringen Sie das zweite Argument `mapFn`, um jedes Element auf seinen Index abzubilden.

Hier ist ein Beispielcodeausschnitt:

```js
const initializeMappedArray = (n, mapFn = (_, i) => i) =>
  Array(n).fill(null).map(mapFn);
```

Sie können die `initializeMappedArray`-Funktion verwenden, um ein abgebildetes Array mit den gewünschten Werten zu erstellen:

```js
initializeMappedArray(5); // [0, 1, 2, 3, 4]
initializeMappedArray(5, (i) => `item ${i + 1}`);
// ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
```
