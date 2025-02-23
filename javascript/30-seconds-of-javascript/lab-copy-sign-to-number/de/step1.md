# Funktion, um das Vorzeichen einer Zahl auf eine andere zu übertragen

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die `copySign`-Funktion gibt den absoluten Wert der ersten Zahl zurück, aber mit dem Vorzeichen der zweiten Zahl. Um dies zu erreichen:

1. Verwenden Sie `Math.sign()`, um zu überprüfen, ob die beiden Zahlen das gleiche Vorzeichen haben.
2. Geben Sie `x` zurück, wenn dies der Fall ist, andernfalls `-x`.

Hier ist der Code für die `copySign`-Funktion:

```js
const copySign = (x, y) => (Math.sign(x) === Math.sign(y) ? x : -x);
```

Sie können die Funktion mit dem folgenden Code testen:

```js
copySign(2, 3); // 2
copySign(2, -3); // -2
copySign(-2, 3); // 2
copySign(-2, -3); // -2
```
