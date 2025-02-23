# Rechter Teilzeichenfolgen-Generator

Um alle rechten Teilzeichenfolgen einer gegebenen Zeichenfolge zu generieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `String.prototype.length`, um die Iteration frühzeitig zu beenden, wenn die Zeichenfolge leer ist.
3. Verwenden Sie eine `for...in`-Schleife und `String.prototype.slice()`, um jede Teilzeichenfolge der gegebenen Zeichenfolge, beginnend am Ende, zu `yield`.

Hier ist der Codeausschnitt:

```js
const rightSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(-i - 1);
};
```

Beispielverwendung:

```js
[...rightSubstrGenerator("hello")];
// [ 'o', 'lo', 'llo', 'ello', 'hello' ]
```
