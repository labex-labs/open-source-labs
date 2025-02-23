# Abgebildete Arraysymmetrische Differenz

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion gibt die symmetrische Differenz zwischen zwei Arrays zurück, nachdem die bereitgestellte Funktion auf jedes Element beider Arrays angewendet wurde. So funktioniert es:

- Erstellen Sie aus jedem Array einen `Set`, um die einzigartigen Werte jedes Arrays zu erhalten, nachdem `fn` auf sie angewendet wurde.
- Verwenden Sie `Array.prototype.filter()` auf jedem von ihnen, um nur die Werte zu behalten, die nicht in dem anderen enthalten sind.

Hier ist der Code für die `symmetricDifferenceBy`-Funktion:

```js
const symmetricDifferenceBy = (a, b, fn) => {
  const sA = new Set(a.map((v) => fn(v))),
    sB = new Set(b.map((v) => fn(v)));
  return [
    ...a.filter((x) => !sB.has(fn(x))),
    ...b.filter((x) => !sA.has(fn(x)))
  ];
};
```

Sie können `symmetricDifferenceBy` wie folgt verwenden:

```js
symmetricDifferenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [ 1.2, 3.4 ]
symmetricDifferenceBy(
  [{ id: 1 }, { id: 2 }, { id: 3 }],
  [{ id: 1 }, { id: 2 }, { id: 4 }],
  (i) => i.id
);
// [{ id: 3 }, { id: 4 }]
```
