# Heapsort-Algorithmus

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie 'node' ein. Der folgende Algorithmus sortiert ein Array von Zahlen mit dem Heapsort-Algorithmus. Folgen Sie diesen Schritten:

- Verwenden Sie Rekursion in der Funktion.
- Verwenden Sie den Spread-Operator `(...)`, um das ursprüngliche Array, `arr`, zu klonen.
- Verwenden Sie Closures, um eine Variable, `l`, und eine Funktion `heapify` zu deklarieren.
- Verwenden Sie eine `for-Schleife` und `Math.floor()` in Kombination mit `heapify`, um einen Max-Heap aus dem Array zu erstellen.
- Verwenden Sie eine `for-Schleife`, um den betrachteten Bereich wiederholt zu verengen, indem Sie `heapify` verwenden und die Werte bei Bedarf tauschen, um das klonierte Array zu sortieren.

```js
const heapsort = (arr) => {
  const a = [...arr];
  let l = a.length;
  const heapify = (a, i) => {
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    let max = i;
    if (left < l && a[left] > a[max]) max = left;
    if (right < l && a[right] > a[max]) max = right;
    if (max !== i) {
      [a[max], a[i]] = [a[i], a[max]];
      heapify(a, max);
    }
  };
  for (let i = Math.floor(l / 2); i >= 0; i -= 1) heapify(a, i);
  for (let i = a.length - 1; i > 0; i--) {
    [a[0], a[i]] = [a[i], a[0]];
    l--;
    heapify(a, 0);
  }
  return a;
};
```

Beispiel:

```js
heapsort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
