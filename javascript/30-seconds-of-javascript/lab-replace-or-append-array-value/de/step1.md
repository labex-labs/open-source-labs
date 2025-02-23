# Wie man Array-Werte ersetzt oder anhängt

Um ein Element in einem Array zu ersetzen oder es hinzuzufügen, wenn es nicht existiert, folgen Sie diesen Schritten:

1. Verwenden Sie den Spread-Operator (`...`), um eine flache Kopie des Arrays zu erstellen.
2. Verwenden Sie `Array.prototype.findIndex()`, um den Index des ersten Elements zu finden, das der bereitgestellten Vergleichsfunktion `compFn` entspricht.
3. Wenn kein solches Element gefunden wird, verwenden Sie `Array.prototype.push()`, um den neuen Wert an das Array anzuhängen.
4. Andernfalls verwenden Sie `Array.prototype.splice()`, um den Wert an der gefundenen Position durch den neuen Wert zu ersetzen.

Hier ist ein Beispiel, wie diese Funktionalität implementiert werden kann:

```js
const replaceOrAppend = (arr, val, compFn) => {
  const res = [...arr];
  const i = arr.findIndex((v) => compFn(v, val));
  if (i === -1) res.push(val);
  else res.splice(i, 1, val);
  return res;
};
```

Sie können diese Funktion mit einem Array von Objekten wie folgt verwenden:

```js
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 28 }
];
const jane = { name: "Jane", age: 29 };
const jack = { name: "Jack", age: 28 };
replaceOrAppend(people, jane, (a, b) => a.name === b.name);
// [ { name: 'John', age: 30 }, { name: 'Jane', age: 29 } ]
replaceOrAppend(people, jack, (a, b) => a.name === b.name);
// [
//   { name: 'John', age: 30 },
//   { name: 'Jane', age: 28 },
//   { name: 'Jack', age: 28 }
// ]
```
