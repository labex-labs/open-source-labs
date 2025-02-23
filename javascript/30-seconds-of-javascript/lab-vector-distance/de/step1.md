# Vektordistanzberechnung

Um die Distanz zwischen zwei Vektoren zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH, um mit der Codeausführung zu beginnen.
2. Geben Sie `node` ein, um zu beginnen.
3. Verwenden Sie `Array.prototype.reduce()`, `Math.pow()` und `Math.sqrt()`, um die euklidische Distanz zwischen den Vektoren zu finden.
4. Wenden Sie die `vectorDistance`-Formel an, die unten gezeigt wird:

```js
const vectorDistance = (x, y) =>
  Math.sqrt(x.reduce((acc, val, i) => acc + Math.pow(val - y[i], 2), 0));
```

5. Testen Sie die Formel, indem Sie zwei Vektoren im folgenden Format eingeben: `vectorDistance([10, 0, 5], [20, 0, 10]);`
6. Die Ausgabe wird die Distanz zwischen den beiden Vektoren sein: `11.180339887498949`.
