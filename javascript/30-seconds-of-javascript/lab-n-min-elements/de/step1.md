# Funktion, um die n kleinsten Elemente eines Arrays zurückzugeben

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Verwenden Sie die `minN`-Funktion, um die `n` kleinsten Elemente eines Arrays zurückzugeben.

So verwenden Sie die Funktion:

- Verwenden Sie `Array.prototype.sort()` und den Spread-Operator (`...`), um einen flachen Klon des Arrays zu erstellen und es aufsteigend zu sortieren.
- Verwenden Sie `Array.prototype.slice()`, um die angegebene Anzahl von Elementen zu erhalten.
- Wenn Sie das zweite Argument, `n`, weglassen, gibt die Funktion ein ein-Element-Array zurück.
- Wenn `n` größer oder gleich der Länge des bereitgestellten Arrays ist, gibt die Funktion das ursprüngliche Array zurück, sortiert in aufsteigender Reihenfolge.

```js
const minN = (arr, n = 1) => [...arr].sort((a, b) => a - b).slice(0, n);
```

Hier sind einige Beispiele:

```js
minN([1, 2, 3]); // [1]
minN([1, 2, 3], 2); // [1, 2]
```
