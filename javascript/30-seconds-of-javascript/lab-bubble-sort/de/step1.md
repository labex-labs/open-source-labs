# Bubblesort-Algorithmus

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu starten. Der Bubblesort-Algorithmus sortiert ein Array von Zahlen.

Schritte zum Sortieren eines Arrays mit dem Bubblesort-Algorithmus:

1. Deklarieren Sie eine Variable `swapped`, die angibt, ob während der aktuellen Iteration Werte getauscht wurden.

2. Verwenden Sie den Spread-Operator (`...`), um das ursprüngliche Array `arr` zu klonen.

3. Verwenden Sie eine `for-Schleife`, um über die Elemente des geklonten Arrays zu iterieren, wobei die Schleife vor dem letzten Element endet.

4. Verwenden Sie eine geschachtelte `for-Schleife`, um über den Abschnitt des Arrays zwischen `0` und `i` zu iterieren, tauschen Sie beliebige benachbarte ungeordnete Elemente aus und legen Sie `swapped` auf `true` fest.

5. Wenn `swapped` nach einer Iteration `false` ist, sind keine weiteren Änderungen erforderlich, daher wird das geklonte Array zurückgegeben.

Beispielcode:

```js
const bubbleSort = (arr) => {
  let swapped = false;
  const a = [...arr];
  for (let i = 1; i < a.length; i++) {
    swapped = false;
    for (let j = 0; j < a.length - i; j++) {
      if (a[j + 1] < a[j]) {
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        swapped = true;
      }
    }
    if (!swapped) return a;
  }
  return a;
};

bubbleSort([2, 1, 4, 3]); // [1, 2, 3, 4]
```
