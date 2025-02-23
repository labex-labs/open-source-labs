# Wie man in JavaScript die Ähnlichkeit von Arrays findet

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Dies hilft Ihnen zu verstehen, wie man ein Array von Elementen findet, die in beiden Arrays auftauchen. Folgen Sie diesen Schritten:

1. Verwenden Sie die `Array.prototype.includes()`-Methode, um die Werte zu bestimmen, die kein Teil von `values` sind.
2. Verwenden Sie die `Array.prototype.filter()`-Methode, um sie zu entfernen.

Hier ist der Code, um die Arrayähnlichkeit zu finden:

```js
const similarity = (arr, values) => arr.filter((v) => values.includes(v));
```

Sie können diesen Code testen, indem Sie den folgenden Befehl ausführen:

```js
similarity([1, 2, 3], [1, 2, 4]); // [1, 2]
```

Dies wird `[1, 2]` als Ausgabe zurückgeben.
