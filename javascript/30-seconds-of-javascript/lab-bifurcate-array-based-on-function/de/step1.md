# Funktion zum Teilen eines Arrays in zwei Gruppen

Um ein Array in zwei Gruppen basierend auf dem Ergebnis einer gegebenen Funktion zu teilen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie die `Array.prototype.reduce()`- und `Array.prototype.push()`-Methoden, um Elemente zu den Gruppen hinzuzufügen. Dies basiert auf dem von der gegebenen Funktion `fn` für jedes Element zurückgegebenen Wert.
3. Wenn `fn` für irgendein Element einen wahren Wert zurückgibt, fügen Sie es zur ersten Gruppe hinzu. Andernfalls fügen Sie es zur zweiten Gruppe hinzu.

Hier ist der Code:

```js
const bifurcateBy = (arr, fn) =>
  arr.reduce(
    (acc, val, i) => (acc[fn(val, i) ? 0 : 1].push(val), acc),
    [[], []]
  );
```

Beispielsweise wird, wenn Sie `bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b')` aufrufen, die Funktion `[ ['beep', 'boop', 'bar'], ['foo'] ]` zurückgeben.
