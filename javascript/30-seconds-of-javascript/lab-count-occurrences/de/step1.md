# Wie man in JavaScript Vorkommen zählt

Um die Anzahl der Vorkommen eines bestimmten Werts in einem JavaScript-Array zu zählen, können Sie die `Array.prototype.reduce()`-Methode verwenden.

So geht es vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Kopieren Sie und fügen Sie folgenden Code ein:

```js
const countOccurrences = (arr, val) =>
  arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
```

3. Im obigen Code nimmt die `countOccurrences`-Funktion zwei Argumente entgegen: das Array, in dem gesucht werden soll, und der Wert, dessen Vorkommen gezählt werden soll.
4. Die `reduce()`-Methode wird verwendet, um durch jedes Element im Array zu iterieren und einen Zähler um 1 zu erhöhen, wenn der spezifische Wert gefunden wird.
5. Um die Funktion zu testen, rufen Sie sie mit einem Array und einem Wert auf, wie folgt:

```js
countOccurrences([1, 1, 2, 1, 2, 3], 1); // 3
```

Dies wird die Anzahl der Vorkommen von `1` im Array `[1, 1, 2, 1, 2, 3]` zurückgeben, die `3` ist.
