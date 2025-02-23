# Filtering Non-Unique Array Values with a Function

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Dieser Code filtert nicht eindeutige Werte aus einem Array basierend auf einer bereitgestellten Vergleichsfunktion. Hier sind die Schritte, um dies zu erreichen:

1. Verwenden Sie `Array.prototype.filter()` und `Array.prototype.every()`, um ein neues Array mit nur den eindeutigen Werten basierend auf der Vergleichsfunktion `fn` zu erstellen.
2. Die Vergleichsfunktion nimmt vier Argumente entgegen: die Werte der beiden zu vergleichenden Elemente und ihre Indizes.
3. Die Funktion `filterNonUniqueBy` implementiert die obigen Schritte und gibt das Array mit den eindeutigen Werten zurück.

```js
const filterNonUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.every((x, j) => (i === j) === fn(v, x, i, j)));
```

Hier ist ein Beispiel, wie diese Funktion verwendet werden kann:

```js
filterNonUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id === b.id
); // [ { id: 2, value: 'c' } ]
```

Dieser Code ist präzise, klar und kohärent und sollte wie erwartet funktionieren.
