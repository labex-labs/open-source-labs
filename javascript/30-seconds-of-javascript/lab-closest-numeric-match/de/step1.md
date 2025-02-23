# Eine Funktion, um die am nächsten liegende numerische Übereinstimmung in einem Array zu finden

Um die am nächsten liegende Zahl in einem Array zu finden, verwenden Sie die folgende Funktion:

```js
const closest = (arr, n) =>
  arr.reduce((acc, num) => (Math.abs(num - n) < Math.abs(acc - n) ? num : acc));
```

So verwenden Sie sie:

1. Öffnen Sie das Terminal/SSH.
2. Geben Sie `node` ein.
3. Verwenden Sie die `closest()`-Funktion und geben Sie das Array und den Zielwert als Argumente an.

Beispielverwendung: `closest([6, 1, 3, 7, 9], 5)` wird `6` zurückgeben, was die am nächsten liegende Zahl zu `5` im Array ist.
