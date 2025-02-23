# Überprüfen, ob eine Zahl teilbar ist

Um in JavaScript zu überprüfen, ob eine Zahl durch eine andere Zahl teilbar ist, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den Modulo-Operator (`%`), um zu überprüfen, ob der Rest der Division gleich `0` ist. Wenn ja, ist die Zahl teilbar.

Hier ist eine Beispiel-Funktion, die überprüft, ob der erste numerische Argument durch das zweite teilbar ist:

```js
const isDivisible = (dividend, divisor) => dividend % divisor === 0;
```

Sie können diese Funktion mit `isDivisible(6, 3)` testen, was `true` zurückgeben sollte, da 6 durch 3 teilbar ist.
