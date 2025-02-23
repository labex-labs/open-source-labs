# Entfernen von Array-Elementen basierend auf einer Funktion

Um bestimmte Elemente aus einem Array zu entfernen, verwenden Sie die `dropWhile`-Funktion, die Elemente entfernt, bis die übergebene Funktion `true` zurückgibt. Die Funktion gibt dann die verbleibenden Elemente im Array zurück.

So funktioniert es:

- Iterieren Sie über das Array mit `Array.prototype.slice()`, um das erste Element des Arrays zu entfernen, bis der Wert, der von `func` zurückgegeben wird, `true` ist.
- Geben Sie die verbleibenden Elemente zurück.

Beispielverwendung:

```js
const dropWhile = (arr, func) => {
  while (arr.length > 0 && !func(arr[0])) arr = arr.slice(1);
  return arr;
};

dropWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
