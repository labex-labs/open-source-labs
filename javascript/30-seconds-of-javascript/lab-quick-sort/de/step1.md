# Quick Sort-Algorithmus

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Dieser Algorithmus sortiert ein Array von Zahlen mithilfe des Quicksort-Algorithmus. Hier sind die Schritte, die Sie zu befolgen haben:

- Verwenden Sie Rekursion.
- Verwenden Sie den Spread-Operator (`...`), um das ursprüngliche Array, `arr`, zu klonen.
- Wenn die `length` des Arrays kleiner als `2` ist, geben Sie das klonierte Array zurück.
- Verwenden Sie `Math.floor()`, um den Index des Pivot-Elements zu berechnen.
- Verwenden Sie `Array.prototype.reduce()` und `Array.prototype.push()`, um das Array in zwei Teilarrays zu teilen. Das erste enthält Elemente, die kleiner oder gleich `pivot` sind, und das zweite enthält Elemente, die größer als es sind. Zerlegen Sie das Ergebnis in zwei Arrays.
- Rufen Sie `quickSort()` rekursiv auf den erstellten Teilarrays auf.

Hier ist ein Beispiel, wie Sie diesen Algorithmus implementieren können:

```js
const quickSort = (arr) => {
  const a = [...arr];
  if (a.length < 2) return a;
  const pivotIndex = Math.floor(arr.length / 2);
  const pivot = a[pivotIndex];
  const [lo, hi] = a.reduce(
    (acc, val, i) => {
      if (val < pivot || (val === pivot && i != pivotIndex)) {
        acc[0].push(val);
      } else if (val > pivot) {
        acc[1].push(val);
      }
      return acc;
    },
    [[], []]
  );
  return [...quickSort(lo), pivot, ...quickSort(hi)];
};
```

Um es zu testen, führen Sie den folgenden Befehl aus:

```js
quickSort([1, 6, 1, 5, 3, 2, 1, 4]); // [1, 1, 1, 2, 3, 4, 5, 6]
```
