# Symmetrischer Unterschied von Arrays

Um den symmetrischen Unterschied zwischen zwei Arrays zu finden und doppelte Werte zu berücksichtigen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Erstellen Sie aus jedem Array einen `Set`, um die einzigartigen Werte jedes Arrays zu erhalten.
3. Verwenden Sie `Array.prototype.filter()` auf jedem der beiden Arrays, um nur die Werte zu behalten, die nicht im anderen Array enthalten sind.

Hier ist der Code:

```js
const symmetricDifference = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...a.filter((x) => !sB.has(x)), ...b.filter((x) => !sA.has(x))];
};
```

Sie können die folgenden Beispiele verwenden, um die Funktion zu testen:

```js
symmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
symmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 2, 3]
```
