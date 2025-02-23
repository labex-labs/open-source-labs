# Funktion zum Teilen eines Arrays in zwei Gruppen

Um diese Funktion zu verwenden, um ein Array anhand von Werten in zwei Gruppen aufzuteilen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `bifurcate()`-Funktion, die die Werte anhand des Ergebnisses des gegebenen `filter`-Arrays in zwei Gruppen aufteilt.
3. Um die Funktion zu implementieren, verwenden Sie `Array.prototype.reduce()` und `Array.prototype.push()`, um Elemente den Gruppen hinzuzufügen, basierend auf dem `filter`-Array.
4. Wenn `filter` für irgendein Element einen wahren Wert hat, fügen Sie es der ersten Gruppe hinzu; andernfalls fügen Sie es der zweiten Gruppe hinzu.

Hier ist der Code für die `bifurcate()`-Funktion:

```js
const bifurcate = (arr, filter) =>
  arr.reduce(
    (acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc),
    [[], []]
  );
```

Sie können die `bifurcate()`-Funktion mit einem Array von Werten und einem entsprechenden Filter-Array aufrufen, um die Werte in zwei Gruppen aufzuteilen. Beispiel:

```js
bifurcate(["beep", "boop", "foo", "bar"], [true, true, false, true]);
// [ ['beep', 'boop', 'bar'], ['foo'] ]
```
