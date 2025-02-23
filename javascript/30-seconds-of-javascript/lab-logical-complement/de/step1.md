# Logische Negation

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Um die logische Negation einer Funktion `fn` zu erhalten, verwenden Sie die `complement`-Funktion. Diese Funktion gibt eine andere Funktion zurück, die den logischen Negationsoperator (`!`) auf das Ergebnis anwendet, wenn `fn` mit beliebigen übergebenen Argumenten aufgerufen wird.

Hier ist ein Beispielcodeausschnitt:

```js
const complement =
  (fn) =>
  (...args) =>
    !fn(...args);
```

Um diese Funktion zu verwenden, definieren Sie eine Prädikatsfunktion, z. B. `isEven`, die `true` zurückgibt, wenn eine gegebene Zahl gerade ist. Anschließend können Sie die logische Negation dieser Funktion mit der `complement`-Funktion erhalten, wie unten gezeigt:

```js
const isEven = (num) => num % 2 === 0;
const isOdd = complement(isEven);
isOdd(2); // false
isOdd(3); // true
```
