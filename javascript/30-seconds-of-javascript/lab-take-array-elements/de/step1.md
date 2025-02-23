# Wie man in JavaScript Array-Elemente entfernt

Um Elemente von Anfang eines Arrays in JavaScript zu entfernen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal oder SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Array.prototype.slice()`-Methode, um ein neues Array zu erstellen, aus dem `n` Elemente von Anfang entfernt werden.
3. Verwenden Sie die `take`-Funktion im folgenden Codeausschnitt, um die Logik umzusetzen.

```js
const take = (arr, n = 1) => arr.slice(0, n);
```

Hier ist ein Beispiel, wie die `take`-Funktion verwendet werden kann:

```js
take([1, 2, 3], 5); // [1, 2, 3]
take([1, 2, 3], 0); // []
```

Im ersten Beispiel gibt `take([1, 2, 3], 5)` `[1, 2, 3]` zurück, da das Array nur 3 Elemente enthält. Im zweiten Beispiel gibt `take([1, 2, 3], 0)` `[]` zurück, da keine Elemente vom Anfang des Arrays genommen werden.
