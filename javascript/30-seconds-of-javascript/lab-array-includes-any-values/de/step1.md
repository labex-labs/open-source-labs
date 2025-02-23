# Überprüfen, ob ein Array bestimmte Werte enthält

Um zu beginnen, die Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Um zu überprüfen, ob ein Array mindestens ein Element aus einem anderen Array enthält, verwenden Sie `Array.prototype.some()` und `Array.prototype.includes()`. Hier ist eine Beispiel-Funktion:

```js
const includesAny = (arr, values) => values.some((v) => arr.includes(v));
```

Sie können diese Funktion aufrufen und als Argumente die beiden Arrays übergeben, die Sie vergleichen möchten. Die Funktion wird einen booleschen Wert zurückgeben, der angibt, ob mindestens ein Element von `values` in `arr` enthalten ist. Hier sind einige Beispiele:

```js
includesAny([1, 2, 3, 4], [2, 9]); // true
includesAny([1, 2, 3, 4], [8, 9]); // false
```
