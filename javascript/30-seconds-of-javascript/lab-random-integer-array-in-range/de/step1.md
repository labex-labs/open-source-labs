# Generieren eines zufälligen ganzzahligen Arrays in einem bestimmten Bereich

Um ein Array von zufälligen ganzen Zahlen in einem bestimmten Bereich zu generieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.from()`, um ein leeres Array der gewünschten Länge zu erstellen.
3. Verwenden Sie `Math.random()`, um zufällige Zahlen zu generieren und diese auf den angegebenen Bereich abzubilden. Verwenden Sie `Math.floor()`, um sie in ganze Zahlen umzuwandeln.
4. Die Funktion `randomIntArrayInRange()` nimmt drei Argumente entgegen: `min`, `max` und ein optionales Argument `n` (Standardwert ist 1).
5. Rufen Sie die Funktion `randomIntArrayInRange()` mit den gewünschten Werten für `min`, `max` und `n` auf, um das zufällige ganzzahlige Array zu generieren.

Hier ist der Code:

```js
const randomIntArrayInRange = (min, max, n = 1) =>
  Array.from(
    { length: n },
    () => Math.floor(Math.random() * (max - min + 1)) + min
  );
```

Beispielverwendung:

```js
randomIntArrayInRange(12, 35, 10); // [ 34, 14, 27, 17, 30, 27, 20, 26, 21, 14 ]
```
