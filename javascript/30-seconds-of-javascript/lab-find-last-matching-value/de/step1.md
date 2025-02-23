# JavaScript-Funktion zum Finden des letzten übereinstimmenden Werts

Um das letzte Element in einem Array zu finden, das einer gegebenen Bedingung entspricht, verwenden Sie die folgende JavaScript-Funktion:

```js
const findLast = (arr, fn) => arr.filter(fn).pop();
```

Um diese Funktion zu verwenden, übergeben Sie das Array, das Sie durchsuchen möchten, und eine Funktion, die für die Elemente, die Sie abgleichen möchten, einen wahren Wert zurückgibt.

Beispielsweise wird `findLast([1, 2, 3, 4], n => n % 2 === 1);` `3` zurückgeben, da es die letzte ungerade Zahl im Array findet.

Um mit der Code-Praxis zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
