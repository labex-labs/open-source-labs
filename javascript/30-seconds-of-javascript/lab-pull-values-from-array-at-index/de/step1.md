# Wie man Werte aus einem Array an einem Index extrahiert

Um bestimmte Werte aus einem Array an bestimmten Indizes herauszuziehen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.filter()` und `Array.prototype.includes()`, um die nicht benötigten Werte auszuschließen und sie in einem neuen Array namens `removed` zu speichern.
3. Setzen Sie `Array.prototype.length` auf `0`, um das ursprüngliche Array zu mutieren, indem Sie seine Länge zurücksetzen.
4. Verwenden Sie `Array.prototype.push()`, um das ursprüngliche Array nur mit den extrahierten Werten neu zu befüllen.
5. Verwenden Sie `Array.prototype.push()`, um die entfernten Werte zu verfolgen.
6. Die Funktion `pullAtIndex` nimmt zwei Argumente entgegen: das ursprüngliche Array und ein Array von Indizes, die extrahiert werden sollen.
7. Die Funktion gibt ein Array der entfernten Werte zurück.

Beispielverwendung:

```js
const pullAtIndex = (arr, pullArr) => {
  let removed = [];
  let pulled = arr
    .map((v, i) => (pullArr.includes(i) ? removed.push(v) : v))
    .filter((v, i) => !pullArr.includes(i));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
  return removed;
};

let myArray = ["a", "b", "c", "d"];
let pulled = pullAtIndex(myArray, [1, 3]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
