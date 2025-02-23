# Anweisungen zum Zusammenführen von sortierten Arrays in JavaScript

Um zwei sortierte Arrays in JavaScript zusammenzuführen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den Spread-Operator (`...`), um beide gegebenen Arrays zu klonen.
3. Verwenden Sie `Array.from()`, um ein Array der passenden Länge basierend auf den gegebenen Arrays zu erstellen.
4. Verwenden Sie `Array.prototype.shift()`, um das neu erstellte Array mit den entfernten Elementen der geklonten Arrays zu befüllen.

Hier ist ein Beispielcodeausschnitt, um zwei sortierte Arrays zusammenzuführen:

```js
const mergeSortedArrays = (a, b) => {
  const _a = [...a],
    _b = [...b];
  return Array.from({ length: _a.length + _b.length }, () => {
    if (!_a.length) return _b.shift();
    else if (!_b.length) return _a.shift();
    else return _a[0] > _b[0] ? _b.shift() : _a.shift();
  });
};

console.log(mergeSortedArrays([1, 4, 5], [2, 3, 6])); // Ausgabe: [1, 2, 3, 4, 5, 6]
```

Im obigen Code nimmt die `mergeSortedArrays`-Funktion zwei sortierte Arrays als Argumente entgegen und gibt das zusammengeführte Array zurück, indem die obigen Schritte befolgt werden. Die Ausgabe für den Beispielcode ist `[1, 2, 3, 4, 5, 6]`.
