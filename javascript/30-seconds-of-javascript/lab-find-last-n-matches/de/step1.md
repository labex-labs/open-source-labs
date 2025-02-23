# Anweisungen zum Finden der letzten N Übereinstimmungen

Um die letzten `n` Elemente zu finden, die einer bestimmten Bedingung entsprechen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die unten bereitgestellte `findLastN`-Funktion.
3. Geben Sie ein Array `arr` und eine `matcher`-Funktion an, die für die Elemente, die Sie zu treffen möchten, einen wahren Wert zurückgibt.
4. Optional können Sie auch die Anzahl `n` der Übereinstimmungen angeben, die Sie zurückgeben möchten (Standardwert ist 1).
5. Die Funktion wird die `matcher`-Funktion für jedes Element von `arr` mithilfe einer `for`-Schleife von hinten beginnend ausführen.
6. Wenn ein Element der `matcher`-Bedingung entspricht, wird es mithilfe von `Array.prototype.unshift()` zum Ergebnissarray hinzugefügt, was die Elemente am Anfang des Arrays einfügt.
7. Wenn die Länge des Ergebnissarrays gleich `n` ist, wird die Funktion das Ergebnis zurückgeben.
8. Wenn es keine Übereinstimmungen gibt oder `n` größer ist als die Anzahl der Übereinstimmungen, wird ein leeres Array zurückgegeben.

```js
const findLastN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.unshift(el);
    if (res.length === n) return res;
  }
  return res;
};
```

Hier sind einige Beispiele für die Verwendung der `findLastN`-Funktion:

```js
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [4, 6]
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
