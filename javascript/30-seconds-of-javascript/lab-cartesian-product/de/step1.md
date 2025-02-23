# Kartesisches Produkt

Um das kartesische Produkt von zwei Arrays zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()`, `Array.prototype.map()` und den Spread-Operator (`...`), um alle möglichen Elementpaare aus den beiden Arrays zu generieren.
3. Verwenden Sie folgenden Code:

```js
const cartesianProduct = (a, b) =>
  a.reduce((p, x) => [...p, ...b.map((y) => [x, y])], []);
```

Beispiel:

```js
cartesianProduct(["x", "y"], [1, 2]);
// [['x', 1], ['x', 2], ['y', 1], ['y', 2]]
```

Dies generiert alle möglichen Kombinationen von Elementen aus den beiden Arrays.
