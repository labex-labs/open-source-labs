# Wie man Array-Elemente in JavaScript verschiebt

Um eine bestimmte Anzahl von Elementen ans Ende eines JavaScript-Arrays zu verschieben, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Array.prototype.slice()`-Methode zweimal, um die Elemente nach dem angegebenen Index und die Elemente davor zu erhalten.
3. Verwenden Sie den Spread-Operator (`...`), um die beiden Arrays zu einem einzigen zu kombinieren.
4. Wenn der `offset` negativ ist, werden die Elemente vom Ende bis zum Anfang des Arrays verschoben.

Hier ist ein Beispielcodeausschnitt, der die `offset`-Funktion implementiert:

```js
const offset = (arr, offset) => [...arr.slice(offset), ...arr.slice(0, offset)];
```

Sie können dann die Funktion mit Ihren gewünschten Array- und Offsetwerten aufrufen:

```js
offset([1, 2, 3, 4, 5], 2); // [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2); // [4, 5, 1, 2, 3]
```
