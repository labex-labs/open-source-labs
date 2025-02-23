# Die Entfernung zwischen zwei Punkten berechnen

Um die Entfernung zwischen zwei Punkten zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Math.hypot()`, um die euklidische Entfernung zwischen zwei Punkten zu berechnen.
3. Implementieren Sie den folgenden Code und ersetzen Sie die Werte von `x0`, `y0`, `x1` und `y1` durch die Koordinaten Ihrer Punkte.

```js
const distance = (x0, y0, x1, y1) => Math.hypot(x1 - x0, y1 - y0);
```

Hier ist ein Beispiel, wie diese Funktion verwendet werden kann:

```js
distance(1, 1, 2, 3); // ~2.2361
```

Dies wird die Entfernung zwischen den Punkten `(1, 1)` und `(2, 3)` ausgeben.
