# Entfernen von Array-Elementen von der Linken Seite

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist eine Funktion, die ein neues Array erstellt, indem eine bestimmte Anzahl von Elementen von der linken Seite entfernt wird:

```js
const drop = (arr, n = 1) => arr.slice(n);
```

Die Funktion verwendet `Array.prototype.slice()`, um die angegebene Anzahl von Elementen von der linken Seite zu entfernen. Wenn Sie das letzte Argument, `n`, weglassen, verwendet die Funktion einen Standardwert von `1`.

Hier sind einige Beispiele für die Verwendung der `drop`-Funktion:

```js
drop([1, 2, 3]); // [2, 3]
drop([1, 2, 3], 2); // [3]
drop([1, 2, 3], 42); // []
```
