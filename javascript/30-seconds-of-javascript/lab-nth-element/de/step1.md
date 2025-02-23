# Das n-te Element eines Arrays finden

Um das n-te Element eines Arrays zu finden, folge diesen Schritten:

1. Öffne das Terminal/SSH und tippe `node`, um mit der Programmierung zu beginnen.
2. Verwende `Array.prototype.slice()`, um ein neues Array zu erstellen, das das n-te Element enthält.
3. Wenn der Index außerhalb der Grenzen liegt, gib `undefined` zurück.
4. Lasse das zweite Argument, `n`, weg, um das erste Element des Arrays zu erhalten.

Hier ist ein Beispielcode, der dies implementiert:

```js
const nthElement = (arr, n = 0) =>
  (n === -1 ? arr.slice(n) : arr.slice(n, n + 1))[0];
```

Du kannst diese Funktion mit den folgenden Beispielen testen:

```js
nthElement(["a", "b", "c"], 1); // Ausgabe: 'b'
nthElement(["a", "b", "b"], -3); // Ausgabe: 'a'
```

Indem du diese Schritte folgst, kannst du mit JavaScript leicht das n-te Element eines Arrays finden.
