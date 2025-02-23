# Überprüfen, ob alle Array-Elemente wahr sind

Um zu überprüfen, ob alle Elemente in einer Sammlung wahr (`true`) sind, kannst du die Methode `Array.prototype.every()` verwenden. Diese Methode nimmt eine Prädikatfunktion als Argument entgegen und gibt `true` zurück, wenn die Funktion für alle Elemente im Array zu `true` ausgewertet wird.

Um den Code zu vereinfachen, kannst du eine Funktion namens `all` verwenden, die ein Array und eine optionale Prädikatfunktion als Argumente entgegennimmt. Die Funktion verwendet `Array.prototype.every()`, um zu überprüfen, ob alle Elemente im Array basierend auf der bereitgestellten Funktion `true` zurückgeben. Wenn keine Funktion angegeben wird, wird `Boolean` als Standard verwendet.

Hier ist ein Beispiel, wie die `all`-Funktion verwendet werden kann:

```js
const all = (arr, fn = Boolean) => arr.every(fn);

all([4, 2, 3], (x) => x > 1); // true
all([1, 2, 3]); // true
```
