# Funktion, um Objekt-Schlüssel auszuwählen, die einer bestimmten Bedingung entsprechen

Um Objekt-Schlüssel auszuwählen, die einer bestimmten Bedingung entsprechen, verwenden Sie die `pickBy()`-Funktion. Diese Funktion erstellt ein neues Objekt, das aus den Eigenschaften besteht, für die die gegebene Funktion einen wahren Wert zurückgibt.

- Verwenden Sie `Object.keys()` und `Array.prototype.filter()`, um die Schlüssel zu entfernen, für die `fn` einen falschen Wert zurückgibt.
- Verwenden Sie `Array.prototype.reduce()`, um die gefilterten Schlüssel wieder in ein Objekt mit den entsprechenden Schlüssel-Wert-Paaren umzuwandeln.
- Die Callback-Funktion wird mit zwei Argumenten aufgerufen: (value, key).

Hier ist der Code für die `pickBy()`-Funktion:

```js
const pickBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});
```

Sie können diese Funktion verwenden, um Schlüssel auszuwählen, die einer Bedingung entsprechen. Beispiel:

```js
pickBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number");
// { 'a': 1, 'c': 3 }
```
