# Testen, ob irgendein Array-Element wahrheitswertig ist

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Um zu überprüfen, ob irgendein Element in einer Sammlung auf der Grundlage einer bereitgestellten Funktion `true` zurückgibt, verwenden Sie `Array.prototype.some()`. Wenn Sie die `Boolean`-Funktion als Standard verwenden möchten, können Sie das zweite Argument, `fn`, weglassen.

Hier ist ein Beispielcode:

```js
const any = (arr, fn = Boolean) => arr.some(fn);
```

Sie können es mit den folgenden Beispielen testen:

```js
any([0, 1, 2, 0], (x) => x >= 2); // true
any([0, 0, 1, 0]); // true
```
