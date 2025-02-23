# Stables Sortieren

Um das stabile Sortieren eines Arrays durchzuführen und die ursprünglichen Indizes von Elementen mit gleichen Werten beizubehalten, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.map()`, um jedes Element des Eingabearrays mit seinem entsprechenden Index zu verknüpfen.
3. Verwenden Sie `Array.prototype.sort()` zusammen mit einer `compare`-Funktion, um die Liste zu sortieren, wobei die ursprüngliche Reihenfolge beibehalten wird, wenn die verglichenen Elemente gleich sind.
4. Verwenden Sie `Array.prototype.map()` erneut, um die Arrayelemente zurück in ihre ursprüngliche Form zu konvertieren.
5. Das ursprüngliche Array wird nicht verändert, sondern stattdessen ein neues Array zurückgegeben.

Hier ist eine Implementierung der `stableSort`-Funktion in JavaScript:

```js
const stableSort = (arr, compare) =>
  arr
    .map((item, index) => ({ item, index }))
    .sort((a, b) => compare(a.item, b.item) || a.index - b.index)
    .map(({ item }) => item);
```

Sie können die `stableSort`-Funktion mit einem Array und einer `compare`-Funktion aufrufen, um ein neues Array mit den sortierten Elementen zu erhalten, wie unten gezeigt:

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const stable = stableSort(arr, () => 0); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
