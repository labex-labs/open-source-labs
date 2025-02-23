# Wie man das Minimum und Maximum eines Arrays mithilfe einer angegebenen Funktion findet

Um zu üben, öffnen Sie das Terminal oder SSH und geben Sie `node` ein.

Hier ist eine Funktion, die das Minimum und Maximum eines Arrays basierend auf einer angegebenen Funktion zurückgibt, die die Vergleichsregel festlegt:

```js
const reduceWhich = (arr, comparator = (a, b) => a - b) =>
  arr.reduce((a, b) => (comparator(a, b) >= 0 ? b : a));
```

Um sie zu verwenden, folgen Sie diesen Schritten:

1. Rufen Sie `reduceWhich` mit dem Array auf, das Sie verarbeiten möchten, und der optionalen `comparator`-Funktion.
2. Die `reduceWhich`-Funktion wird `Array.prototype.reduce()` in Kombination mit der `comparator`-Funktion verwenden, um das passende Element im Array zurückzugeben.
3. Wenn Sie das zweite Argument (`comparator`) weglassen, wird die Standardfunktion verwendet, die das kleinste Element im Array zurückgibt.

Hier sind einige Beispiele dafür, wie man `reduceWhich` verwendet:

```js
reduceWhich([1, 3, 2]); // 1
reduceWhich([1, 3, 2], (a, b) => b - a); // 3
reduceWhich(
  [
    { name: "Tom", age: 12 },
    { name: "Jack", age: 18 },
    { name: "Lucy", age: 9 }
  ],
  (a, b) => a.age - b.age
); // {name: 'Lucy', age: 9}
```

In den obigen Beispielen gibt der erste Aufruf von `reduceWhich` den kleinsten Wert des Arrays `[1, 3, 2]` zurück, der `1` ist. Der zweite Aufruf gibt den größten Wert des gleichen Arrays basierend auf der `comparator`-Funktion zurück, die die Vergleichsreihenfolge umkehrt. Der dritte Aufruf gibt das Objekt im Array zurück, das die kleinste `age`-Eigenschaft hat, basierend auf der `comparator`-Funktion, die die `age`-Eigenschaften der Objekte vergleicht.
