# Insertionsort-Algorithmus in JavaScript

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Dieser Algorithmus sortiert ein Array von Zahlen mit der Insertionsort-Methode. Folgen Sie diesen Schritten, um diesen Algorithmus zu implementieren:

1. Verwenden Sie `Array.prototype.reduce()`, um über alle Elemente im gegebenen Array zu iterieren.
2. Wenn die `length` des Akkumulators `0` ist, fügen Sie das aktuelle Element hinzu.
3. Verwenden Sie `Array.prototype.some()`, um über die Ergebnisse im Akkumulator zu iterieren, bis die richtige Position gefunden ist.
4. Verwenden Sie `Array.prototype.splice()`, um das aktuelle Element in den Akkumulator einzufügen.

Hier ist der Code, um den Insertionsort in JavaScript zu implementieren:

```js
const insertionSort = (arr) =>
  arr.reduce((acc, x) => {
    if (!acc.length) return [x];
    acc.some((y, j) => {
      if (x <= y) {
        acc.splice(j, 0, x);
        return true;
      }
      if (x > y && j === acc.length - 1) {
        acc.splice(j + 1, 0, x);
        return true;
      }
      return false;
    });
    return acc;
  }, []);
```

Sie können den Algorithmus mit dem folgenden Code testen:

```js
insertionSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
