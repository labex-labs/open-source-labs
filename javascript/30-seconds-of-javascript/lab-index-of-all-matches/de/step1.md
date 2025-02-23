# Alle Übereinstimmungen-Index

Um alle Indizes von `val` in einem Array zu finden, verwenden Sie `Array.prototype.reduce()`, um über die Elemente zu iterieren und die Indizes für übereinstimmende Elemente zu speichern. Wenn `val` nie vorkommt, wird ein leeres Array zurückgegeben.

```js
const indexOfAll = (arr, val) =>
  arr.reduce((acc, el, i) => (el === val ? [...acc, i] : acc), []);
```

Beispielverwendung:

```js
indexOfAll([1, 2, 3, 1, 2, 3], 1); // [0, 3]
indexOfAll([1, 2, 3], 4); // []
```

Um zu beginnen, mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Dies ist ein Index aller Übereinstimmungen.
