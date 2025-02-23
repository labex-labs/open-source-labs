# Wie man überprüft, ob eine Zahl Dezimalzahlen aufweist

Um zu überprüfen, ob eine Zahl Dezimalzahlen aufweist, kannst du den Modulo-Operator in JavaScript verwenden. Folge diesen Schritten:

1. Öffne das Terminal/SSH und tippe `node`, um mit der Code-Praxis zu beginnen.
2. Verwende den Modulo-Operator (`%`), um zu überprüfen, ob die Zahl durch `1` teilbar ist.
3. Wenn das Ergebnis nicht gleich null ist, hat die Zahl Dezimalzahlen.

Hier ist ein Beispielcode, um zu überprüfen, ob eine Zahl Dezimalzahlen aufweist:

```js
const hasDecimals = (num) => num % 1 !== 0;
```

Du kannst die Funktion testen, indem du sie mit verschiedenen Zahlen aufrufst, wie folgt:

```js
hasDecimals(1); // false
hasDecimals(1.001); // true
```
