# Iterierbares in Blöcke unterteilen

Um ein Iterierbares in kleinere Arrays einer bestimmten Größe zu unterteilen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie eine `for...of`-Schleife über das gegebene Iterierbare und verwenden Sie `Array.prototype.push()`, um jedes neue Element der aktuellen `chunk` hinzuzufügen.
3. Überprüfen Sie, ob die aktuelle `chunk` die gewünschte `Größe` hat, indem Sie `Array.prototype.length` verwenden, und geben Sie den Wert zurück, wenn dies der Fall ist.
4. Überprüfen Sie die letzte `chunk` mit `Array.prototype.length` und geben Sie sie zurück, wenn sie nicht leer ist.
5. Verwenden Sie folgenden Code:

```js
const chunkify = function* (itr, size) {
  let chunk = [];
  for (const v of itr) {
    chunk.push(v);
    if (chunk.length === size) {
      yield chunk;
      chunk = [];
    }
  }
  if (chunk.length) yield chunk;
};
```

6. Verwenden Sie diesen Code, um die Funktion zu testen:

```js
const x = new Set([1, 2, 1, 3, 4, 1, 2, 5]);
[...chunkify(x, 2)]; // [[1, 2], [3, 4], [5]]
```
