# Wie man ein Array mit JavaScript flachmacht

Um ein Array in JavaScript bis zu einer bestimmten Tiefe zu flachmachen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `flatten`-Funktion mit zwei Argumenten: `arr` (das zu flachende Array) und `depth` (die maximale Anzahl der geschachtelten Ebenen, die geflachtet werden sollen).
3. Innerhalb der `flatten`-Funktion verwenden Sie Rekursion, um `depth` um `1` pro Ebene Tiefe zu verringern.
4. Verwenden Sie `Array.prototype.reduce()` und `Array.prototype.concat()`, um Elemente oder Arrays zu kombinieren.
5. Fügen Sie einen Basisfall hinzu, wenn `depth` gleich `1` ist, um die Rekursion zu beenden.
6. Überspringen Sie das zweite Argument, `depth`, um nur bis zu einer Tiefe von `1` zu flachmachen (einzige Flachmacher).

Hier ist der Code für die `flatten`-Funktion:

```js
const flatten = (arr, depth = 1) =>
  arr.reduce(
    (a, v) =>
      a.concat(depth > 1 && Array.isArray(v) ? flatten(v, depth - 1) : v),
    []
  );
```

Sie können die `flatten`-Funktion mit den folgenden Beispielen testen:

```js
flatten([1, [2], 3, 4]); // [1, 2, 3, 4]
flatten([1, [2, [3, [4, 5], 6], 7], 8], 2); // [1, 2, 3, [4, 5], 6, 7, 8]
```
