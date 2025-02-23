# Wie man die letzten n Elemente eines Arrays in JavaScript erhält

Um die letzten `n` Elemente eines Arrays in JavaScript zu erhalten, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Verwenden Sie `Array.prototype.slice()` mit einem Startwert von `-n`, um die letzten `n` Elemente des Arrays zu erhalten.

Hier ist der JavaScript-Code, um die letzten `n` Elemente eines Arrays zu erhalten:

```js
const lastN = (arr, n) => arr.slice(-n);
```

Um den Code zu testen, rufen Sie die `lastN()`-Funktion mit dem Array und der Anzahl der Elemente auf, die Sie erhalten möchten, wie folgt:

```js
lastN(["a", "b", "c", "d"], 2); // ['c', 'd']
```
