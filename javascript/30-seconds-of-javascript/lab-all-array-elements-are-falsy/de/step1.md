# Funktion zum Testen, ob alle Array-Elemente falsy sind

Um zu testen, ob alle Elemente eines Arrays falsy sind, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.some()`, um zu testen, ob irgendeine Elemente in der Sammlung `true` zurückgeben, basierend auf der bereitgestellten Prädikatfunktion.
3. Wenn Sie das zweite Argument, `fn`, weglassen, verwendet die Funktion `Boolean` als Standard.
4. Die Funktion gibt `true` zurück, wenn alle Elemente im Array falsy sind, und `false` sonst.

Hier ist eine Beispielimplementierung der Funktion:

```js
const none = (arr, fn = Boolean) => !arr.some(fn);
```

Sie können die Funktion wie folgt verwenden:

```js
none([0, 1, 3, 0], (x) => x == 2); // true
none([0, 0, 0]); // true
```
