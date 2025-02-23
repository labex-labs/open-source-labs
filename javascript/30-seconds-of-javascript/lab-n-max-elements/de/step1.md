# Wie man in JavaScript die n größten Elemente aus einem Array bekommt

Um in JavaScript zu programmieren, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Nachdem Sie das getan haben, können Sie die folgenden Schritte verwenden, um die `n` größten Elemente aus einem Array zu erhalten:

1. Verwenden Sie `Array.prototype.sort()` zusammen mit dem Spread-Operator (`...`), um eine flache Kopie des Arrays zu erstellen und es in absteigender Reihenfolge zu sortieren.
2. Verwenden Sie `Array.prototype.slice()`, um die angegebene Anzahl von Elementen zu erhalten.
3. Wenn Sie das zweite Argument, `n`, weglassen, erhalten Sie standardmäßig ein Array mit einem Element.
4. Wenn `n` größer als oder gleich der Länge des bereitgestellten Arrays ist, dann geben Sie das ursprüngliche Array zurück (in absteigender Reihenfolge sortiert).

Hier ist der JavaScript-Code für die `maxN`-Funktion, die diese Schritte implementiert:

```js
const maxN = (arr, n = 1) => [...arr].sort((a, b) => b - a).slice(0, n);
```

Sie können die `maxN`-Funktion mit den folgenden Beispielen testen:

```js
maxN([1, 2, 3]); // [3]
maxN([1, 2, 3], 2); // [3, 2]
```
