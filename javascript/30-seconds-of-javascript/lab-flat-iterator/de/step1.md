# Erklärung des flachen Iterators

Um einen Generator zu erstellen, der über ein Iterierbares iteriert und geschachtelte Iterierbare zusammenflacht, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie Rekursion in der Generatorfunktion.
3. Verwenden Sie eine `for...of`-Schleife, um über die Werte des gegebenen Iterierbaren zu iterieren.
4. Verwenden Sie `Symbol.iterator`, um zu überprüfen, ob jeder Wert ein Iterierbares ist.
5. Wenn ja, verwenden Sie den `yield*`-Ausdruck, um rekursiv an die gleiche Generatorfunktion weiterzugeben.
6. Andernfalls geben Sie den aktuellen Wert mit `yield` zurück.

Hier ist ein Beispielcodeausschnitt:

```js
const flatIterator = function* (itr) {
  for (let item of itr) {
    if (item[Symbol.iterator]) yield* flatIterator(item);
    else yield item;
  }
};

const arr = [1, 2, [3, 4], [5, [6, [7], 8]], 9, new Set([10, 11])];
[...flatIterator(arr)]; // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
```

Im Beispiel ist `arr` ein Array von Werten, einschließlich geschachtelter Arrays und einer Menge. Die `flatIterator`-Generatorfunktion wird verwendet, um diese geschachtelten Werte zusammenzuziehen und ein zusammengezogenes Array zurückzugeben.
