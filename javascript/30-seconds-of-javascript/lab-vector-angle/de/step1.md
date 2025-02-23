# Vektorkosinusberechnung

Um den Winkel (Theta) zwischen zwei Vektoren zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()`, `Math.pow()` und `Math.sqrt()`, um die Länge jedes Vektors und das Skalarprodukt der beiden Vektoren zu berechnen.
3. Verwenden Sie `Math.acos()`, um den Arkuskosinus zu berechnen und den Theta-Wert zu erhalten.

Hier ist ein Beispielcodeausschnitt:

```js
const vectorAngle = (x, y) => {
  let mX = Math.sqrt(x.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  let mY = Math.sqrt(y.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  return Math.acos(x.reduce((acc, n, i) => acc + n * y[i], 0) / (mX * mY));
};

vectorAngle([3, 4], [4, 3]); // 0.283794109208328
```

Diese Funktion nimmt zwei Arrays (`x` und `y`) als Argumente entgegen und gibt den Winkel (in Radiant) zwischen ihnen zurück.
