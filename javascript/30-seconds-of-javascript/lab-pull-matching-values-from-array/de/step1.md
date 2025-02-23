# Wie man passende Werte aus einem Array extrahiert

Um bestimmte Werte aus einem Array mit JavaScript zu extrahieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.filter()` und `Array.prototype.includes()`, um die nicht benötigten Werte auszuschließen und ein neues Array zu erstellen.
3. Legen Sie `Array.prototype.length` fest, um das ursprüngliche Array zu verändern, indem Sie seine Länge auf `0` zurücksetzen.
4. Verwenden Sie `Array.prototype.push()`, um das ursprüngliche Array nur mit den extrahierten Werten neu zu befüllen.
5. Verwenden Sie `Array.prototype.push()`, um die entfernten Werte in einem neuen Array zu verfolgen.

Hier ist eine Beispiel-Funktion, die diese Schritte implementiert:

```js
const pullAtValue = (arr, pullArr) => {
  let removed = [],
    pushToRemove = arr.forEach((v, i) =>
      pullArr.includes(v) ? removed.push(v) : v
    ),
    mutateTo = arr.filter((v, i) => !pullArr.includes(v));
  arr.length = 0;
  mutateTo.forEach((v) => arr.push(v));
  return removed;
};
```

Sie können diese Funktion verwenden, um bestimmte Werte aus einem Array zu entfernen und die entfernten Elemente wie folgt zurückzugeben:

```js
let myArray = ["a", "b", "c", "d"];
let pulled = pullAtValue(myArray, ["b", "d"]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
