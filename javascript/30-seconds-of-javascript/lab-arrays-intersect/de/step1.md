# Wie man überprüft, ob zwei Arrays ein gemeinsames Element haben

Um zu überprüfen, ob zwei Arrays ein gemeinsames Element haben, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Erstellen Sie aus `b` einen `Set`, um die eindeutigen Werte in `b` zu erhalten.
3. Verwenden Sie `Array.prototype.some()` auf `a`, um zu überprüfen, ob irgendeiner seiner Werte in `b` enthalten ist, indem Sie `Set.prototype.has()` verwenden.
4. Verwenden Sie die unten bereitgestellte `intersects`-Funktion, um die Arrays zu testen.

```js
const intersects = (a, b) => {
  const s = new Set(b);
  return [...new Set(a)].some((x) => s.has(x));
};
```

Verwenden Sie die `intersects`-Funktion, um zu überprüfen, ob zwei Arrays sich überschneiden:

```js
intersects(["a", "b"], ["b", "c"]); // true
intersects(["a", "b"], ["c", "d"]); // false
```

Indem Sie diese Schritte befolgen und den bereitgestellten Code verwenden, können Sie leicht überprüfen, ob zwei Arrays ein gemeinsames Element haben.
