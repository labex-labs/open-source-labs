# Wie man das Produkt von numerischen Werten in JavaScript berechnet

Um das Produkt von zwei oder mehr Zahlen oder Arrays in JavaScript zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Array.prototype.reduce()`-Methode, um jedes Element mit einem Akkumulator zu multiplizieren, der mit dem Wert `1` initialisiert werden sollte.
3. Definieren Sie eine Funktion namens `prod`, die beliebig viele Argumente mit dem Spread-Operator (`...`) annimmt. Innerhalb der Funktion wenden Sie die `reduce()`-Methode auf das aufgespaltene Array der Argumente an.
4. Die Funktion gibt das Ergebnis der Multiplikation zurück.

Hier ist ein Beispiel, wie die `prod`-Funktion verwendet werden kann:

```js
const prod = (...arr) => [...arr].reduce((acc, val) => acc * val, 1);

prod(1, 2, 3, 4); // 24
prod(...[1, 2, 3, 4]); // 24
```

Im obigen Beispiel geben `prod(1, 2, 3, 4)` und `prod(...[1, 2, 3, 4])` beide `24` zurück.
