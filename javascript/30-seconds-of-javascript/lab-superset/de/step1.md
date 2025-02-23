# Funktion, um zu überprüfen, ob eine Menge eine Supermenge einer anderen Menge ist

Um zu überprüfen, ob eine Menge eine Supermenge einer anderen Menge ist, verwenden Sie die `superSet()`-Funktion. Öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen. Verwenden Sie dann die folgenden Schritte:

- Erstellen Sie aus jeder Iterable ein neues `Set`-Objekt, indem Sie den `Set`-Konstruktor verwenden.
- Verwenden Sie `Array.prototype.every()` und `Set.prototype.has()`, um zu überprüfen, ob jeder Wert in der zweiten Iterable im ersten enthalten ist.
- Die Funktion gibt `true` zurück, wenn die erste Iterable eine Supermenge der zweiten ist, wobei Duplikatewerte ausgeschlossen sind. Andernfalls gibt sie `false` zurück.

```js
const superSet = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sB].every((v) => sA.has(v));
};
```

Verwenden Sie `superSet()` mit zwei Mengen als Argumenten, um zu überprüfen, ob eine Menge eine Supermenge einer anderen Menge ist.

```js
superSet(new Set([1, 2, 3, 4]), new Set([1, 2])); // true
superSet(new Set([1, 2, 3, 4]), new Set([1, 5])); // false
```
