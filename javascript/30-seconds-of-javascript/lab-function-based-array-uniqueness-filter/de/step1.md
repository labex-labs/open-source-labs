# Filter Unique Array Values Based on Function

Hier ist, wie man ein Array erstellt, das nur die nicht-eindeutigen Werte enthält, indem man die eindeutigen Werte anhand einer Vergleichsfunktion, `fn`, herausfiltert:

```js
const filterUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.some((x, j) => (i !== j) === fn(v, x, i, j)));
```

Um diese Funktion zu verwenden, rufen Sie `filterUniqueBy()` mit zwei Argumenten auf: das Array, das Sie filtern möchten, und die Vergleichsfunktion. Die Vergleichsfunktion sollte vier Argumente akzeptieren: die Werte der beiden zu vergleichenden Elemente und ihre Indizes.

Beispielsweise, wenn Sie ein Array von Objekten haben und die Objekte mit eindeutigen `id`-Werten herausfiltern möchten, können Sie das folgendermaßen tun:

```js
filterUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 3, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 0, value: 'e' } ]
```

Um zu beginnen, mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
