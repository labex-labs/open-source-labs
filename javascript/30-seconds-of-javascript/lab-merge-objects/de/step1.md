# Objekt-Merge-Funktion

Um zwei oder mehr Objekte zu kombinieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen zu programmieren.
2. Verwenden Sie `Array.prototype.reduce()` zusammen mit `Object.keys()`, um über alle Objekte und Schlüssel zu iterieren.
3. Verwenden Sie `Object.prototype.hasOwnProperty()` und `Array.prototype.concat()`, um die Werte für Schlüssel, die in mehreren Objekten vorhanden sind, anzuhängen.
4. Verwenden Sie den angegebenen Codeausschnitt, um ein neues Objekt aus der Kombination von zwei oder mehr Objekten zu erstellen.

```js
const merge = (...objs) =>
  [...objs].reduce(
    (acc, obj) =>
      Object.keys(obj).reduce((a, k) => {
        acc[k] = acc.hasOwnProperty(k)
          ? [].concat(acc[k]).concat(obj[k])
          : obj[k];
        return acc;
      }, {}),
    {}
  );
```

Beispielsweise betrachten Sie die folgenden Objekte:

```js
const object = {
  a: [{ x: 2 }, { y: 4 }],
  b: 1
};
const other = {
  a: { z: 3 },
  b: [2, 3],
  c: "foo"
};
```

Wenn Sie diese beiden Objekte mit der `merge()`-Funktion kombinieren, erhalten Sie das folgende Ergebnis:

```js
merge(object, other);
// { a: [ { x: 2 }, { y: 4 }, { z: 3 } ], b: [ 1, 2, 3 ], c: 'foo' }
```
