# Arrayunterschied

Um den Unterschied zwischen zwei Arrays zu finden, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen zu codieren.

2. Erstellen Sie aus Array `b` einen `Set`, um die eindeutigen Werte aus `b` zu extrahieren.

3. Verwenden Sie `Array.prototype.filter()` auf Array `a`, um nur die Werte zu behalten, die nicht im Array `b` sind, indem Sie `Set.prototype.has()` verwenden.

Hier ist der Code:

```js
const difference = (a, b) => {
  const s = new Set(b);
  return a.filter((x) => !s.has(x));
};
```

Beispielverwendung:

```js
difference([1, 2, 3, 3], [1, 2, 4]); // Ausgabe: [3, 3]
```
