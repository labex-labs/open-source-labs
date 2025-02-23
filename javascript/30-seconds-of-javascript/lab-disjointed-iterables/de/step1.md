# Prüfen auf disjunkte Iterierbare

Um zu überprüfen, ob zwei Iterierbare keine gemeinsamen Werte haben, können Sie die `isDisjoint`-Funktion verwenden.

So verwenden Sie sie:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Erstellen Sie aus jedem Iterierbare ein neues `Set`-Objekt, indem Sie den `Set`-Konstruktor verwenden.
3. Verwenden Sie `Array.prototype.every()` und `Set.prototype.has()`, um zu überprüfen, dass die beiden Iterierbare keine gemeinsamen Werte haben.

```js
const isDisjoint = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sA].every((v) => !sB.has(v));
};
```

Hier sind einige Beispiele:

```js
isDisjoint(new Set([1, 2]), new Set([3, 4])); // true
isDisjoint(new Set([1, 2]), new Set([1, 3])); // false
```
