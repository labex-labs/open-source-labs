# Euklidische Distanzberechnung

Um die Distanz zwischen zwei Punkten in beliebig vielen Dimensionen zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie `Object.keys()` und `Array.prototype.map()`, um jede Koordinate auf ihre Differenz zwischen den beiden Punkten abzubilden.
3. Verwenden Sie `Math.hypot()`, um die euklidische Distanz zwischen den beiden Punkten zu berechnen.

Hier ist ein Beispiel-Codeausschnitt, um Ihnen zu helfen, loszulegen:

```js
const euclideanDistance = (a, b) =>
  Math.hypot(...Object.keys(a).map((k) => b[k] - a[k]));
```

Sie können die Funktion mit diesen Beispiel-Eingaben testen:

```js
euclideanDistance([1, 1], [2, 3]); // ~2.2361
euclideanDistance([1, 1, 1], [2, 3, 2]); // ~2.4495
```
