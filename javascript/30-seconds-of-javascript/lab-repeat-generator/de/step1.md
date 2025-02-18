# Codepraktikum mit Repeat Generator

Um das Codieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein, um einen Generator zu erstellen, der den gegebenen Wert unendlich oft wiederholt. Verwenden Sie eine nicht endende `while`-Schleife, die jedes Mal einen Wert `yield`-ed, wenn `Generator.prototype.next()` aufgerufen wird. Verwenden Sie dann den Rückgabewert der `yield`-Anweisung, um den zurückgegebenen Wert zu aktualisieren, wenn der übergebene Wert nicht `undefined` ist.

```js
const repeatGenerator = function* (val) {
  let v = val;
  while (true) {
    let newV = yield v;
    if (newV !== undefined) v = newV;
  }
};
```

Um den Generator zu testen, erstellen Sie eine Instanz davon mit dem Wert `5` und rufen Sie `repeater.next()` auf, um den nächsten Wert in der Sequenz zu erhalten. Die Ausgabe wird `{ value: 5, done: false }` sein. Wenn Sie `repeater.next()` erneut aufrufen, wird der gleiche Wert zurückgegeben. Um den Wert zu ändern, rufen Sie `repeater.next(4)` auf, was `{ value: 4, done: false }` zurückgeben wird. Schließlich wird das Aufrufen von `repeater.next()` den aktualisierten Wert `{ value: 4, done: false }` zurückgeben.
