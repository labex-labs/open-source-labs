# Objekte nach Bedingung und Schlüsseln filtern

Um ein Array von Objekten anhand einer Bedingung zu filtern und gleichzeitig unspezifizierte Schlüssel auszublenden, verwenden Sie die Funktion `reducedFilter()`.

Hier sind die Schritte, die Sie zu befolgen haben:

1. Verwenden Sie `Array.prototype.filter()`, um das Array anhand des Prädikats `fn` zu filtern, sodass es die Objekte zurückgibt, für die die Bedingung einen wahren Wert zurückgegeben hat.

2. Verwenden Sie `Array.prototype.map()` auf dem gefilterten Array, um das neue Objekt zurückzugeben.

3. Verwenden Sie `Array.prototype.reduce()`, um die Schlüssel auszublenden, die nicht als `keys`-Argument übergeben wurden.

```js
const reducedFilter = (data, keys, fn) =>
  data.filter(fn).map((el) =>
    keys.reduce((acc, key) => {
      acc[key] = el[key];
      return acc;
    }, {})
  );
```

Hier ist ein Beispiel für die Verwendung der `reducedFilter()`-Funktion:

```js
const data = [
  {
    id: 1,
    name: "john",
    age: 24
  },
  {
    id: 2,
    name: "mike",
    age: 50
  }
];

reducedFilter(data, ["id", "name"], (item) => item.age > 24);
// Ausgabe: [{ id: 2, name:'mike'}]
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
