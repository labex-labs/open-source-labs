# Wie man in JavaScript Objekte tief zusammenführt

Um in JavaScript zwei Objekte tief zusammenzuführen, kann man die `deepMerge`-Funktion verwenden. Diese Funktion nimmt zwei Objekte und eine Funktion als Argumente. Die Funktion wird verwendet, um Schlüssel zu verarbeiten, die in beiden Objekten vorhanden sind.

So funktioniert die `deepMerge`-Funktion:

1. Verwenden Sie `Object.keys()`, um die Schlüssel beider Objekte zu erhalten, erstellen Sie daraus einen `Set` und verwenden Sie den Spread-Operator (`...`), um ein Array aller eindeutigen Schlüssel zu erstellen.
2. Verwenden Sie `Array.prototype.reduce()`, um jeden eindeutigen Schlüssel zum Objekt hinzuzufügen, wobei `fn` verwendet wird, um die Werte der beiden gegebenen Objekte zu kombinieren.

Hier ist der Code für die `deepMerge`-Funktion:

```js
const deepMerge = (a, b, fn) =>
  [...new Set([...Object.keys(a), ...Object.keys(b)])].reduce(
    (acc, key) => ({ ...acc, [key]: fn(key, a[key], b[key]) }),
    {}
  );
```

Um die `deepMerge`-Funktion zu verwenden, rufen Sie sie mit zwei Objekten und einer Funktion auf. Hier ist ein Beispiel:

```js
deepMerge(
  { a: true, b: { c: [1, 2, 3] } },
  { a: false, b: { d: [1, 2, 3] } },
  (key, a, b) => (key === "a" ? a && b : Object.assign({}, a, b))
);
// { a: false, b: { c: [ 1, 2, 3 ], d: [ 1, 2, 3 ] } }
```

In diesem Beispiel wird die `deepMerge`-Funktion verwendet, um zwei Objekte zusammenzuführen. Das resultierende Objekt hat die Werte beider Objekte zusammengeführt.
