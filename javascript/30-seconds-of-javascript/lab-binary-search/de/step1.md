# Binärsuche-Algorithmus

Um mit der Codierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Der Binärsuche-Algorithmus wird verwendet, um den Index eines angegebenen Elements in einem sortierten Array zu finden. Hier sind die Schritte, um den Binärsuche-Algorithmus zu implementieren:

1. Deklarieren Sie die linken und rechten Suchgrenzen, `l` und `r`, die initial auf `0` und die `Länge` des Arrays festgelegt werden.
2. Verwenden Sie eine `while-Schleife`, um die Suchuntermenge wiederholt zu verengen, indem Sie sie mit `Math.floor()` halbieren.
3. Wenn das Element gefunden wird, geben Sie seinen Index zurück. Andernfalls geben Sie `-1` zurück.
4. Beachten Sie, dass dieser Algorithmus keine doppelten Werte im Array berücksichtigt.

Hier ist eine Beispielimplementierung des Binärsuche-Algorithmus in JavaScript:

```js
const binarySearch = (arr, item) => {
  let l = 0,
    r = arr.length - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    const guess = arr[mid];
    if (guess === item) return mid;
    if (guess > item) r = mid - 1;
    else l = mid + 1;
  }
  return -1;
};
```

Sie können die `binarySearch`-Funktion mit den folgenden Beispielen testen:

```js
binarySearch([1, 2, 3, 4, 5], 1); // 0
binarySearch([1, 2, 3, 4, 5], 5); // 4
binarySearch([1, 2, 3, 4, 5], 6); // -1
```
