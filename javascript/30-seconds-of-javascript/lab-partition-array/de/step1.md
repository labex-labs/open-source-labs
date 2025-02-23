# Array-Partitionierungsalgorithmus

Um ein Array aufzuteilen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Wenden Sie die bereitgestellte Funktion `fn` auf jedes Element im angegebenen Array `arr` an.
3. Teilen Sie das Array jedes Mal auf, wenn `fn` einen neuen Wert zurückgibt.
4. Verwenden Sie `Array.prototype.reduce()`, um ein Akkumulator-Objekt zu erstellen, das das resultierende Array und den letzten Wert enthält, der von `fn` zurückgegeben wurde.
5. Verwenden Sie `Array.prototype.push()`, um jedes Element in `arr` der entsprechenden Partition im Akkumulator-Array hinzuzufügen.
6. Geben Sie das resultierende Array zurück.

Hier ist die Codeimplementierung:

```js
const partitionBy = (arr, fn) =>
  arr.reduce(
    ({ res, last }, v, i, a) => {
      const next = fn(v, i, a);
      if (next !== last) res.push([v]);
      else res[res.length - 1].push(v);
      return { res, last: next };
    },
    { res: [] }
  ).res;
```

Beispielverwendung:

```js
const numbers = [1, 1, 3, 3, 4, 5, 5, 5];
partitionBy(numbers, (n) => n % 2 === 0); // [[1, 1, 3, 3], [4], [5, 5, 5]]
partitionBy(numbers, (n) => n); // [[1, 1], [3, 3], [4], [5, 5, 5]]
```
