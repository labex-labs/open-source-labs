# Merge Sort-Algorithmus

Um das Programmieren mit dem Merge Sort-Algorithmus zu üben, folgen Sie diesen Schritten:

1. Öffnen Sie die Konsole/SSH und geben Sie `node` ein.
2. Verwenden Sie Rekursion, um ein Array von Zahlen zu sortieren.
3. Wenn die `length` des Arrays kleiner als `2` ist, geben Sie das Array zurück.
4. Verwenden Sie `Math.floor()`, um den Mittelpunkt des Arrays zu berechnen.
5. Verwenden Sie `Array.prototype.slice()`, um das Array in zwei Hälften zu schneiden und rufen Sie `mergeSort()` rekursiv auf den erstellten Teilarrays auf.
6. Schließlich verwenden Sie `Array.from()` und `Array.prototype.shift()`, um die beiden sortierten Teilarrays zu einem einzigen zusammenzufügen.

Hier ist der Code:

```js
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const mid = Math.floor(arr.length / 2);
  const l = mergeSort(arr.slice(0, mid));
  const r = mergeSort(arr.slice(mid, arr.length));
  return Array.from({ length: l.length + r.length }, () => {
    if (!l.length) return r.shift();
    else if (!r.length) return l.shift();
    else return l[0] > r[0] ? r.shift() : l.shift();
  });
};
```

Testen Sie es mit diesem Beispiel:

```js
mergeSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```
