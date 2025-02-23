# Funktion, um die Differenz zweier Arrays mithilfe von Mapping zurückzugeben

Um mit der Programmierung zu beginnen, öffnen Sie Ihr Terminal/SSH und geben Sie `node` ein.

Diese Funktion nimmt zwei Arrays und wendet die bereitgestellte Funktion auf jedes Element in beiden Arrays an, um ihre Differenz zurückzugeben.

Um dies zu tun:

- Erstellen Sie eine `Set`, indem Sie die Funktion (`fn`) auf jedes Element im zweiten Array (`b`) anwenden.
- Verwenden Sie `Array.prototype.map()`, um die Funktion (`fn`) auf jedes Element im ersten Array (`a`) anzuwenden.
- Verwenden Sie `Array.prototype.filter()` in Kombination mit der Funktion (`fn`) auf dem ersten Array (`a`), um nur die Werte zu behalten, die nicht im zweiten Array (`b`) enthalten sind, indem Sie `Set.prototype.has()` verwenden.

Hier ist der Code für die Funktion:

```js
const differenceBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return a.map(fn).filter((el) => !s.has(el));
};
```

Hier sind einige Beispiele dafür, wie die Funktion verwendet werden kann:

```js
differenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [1]
differenceBy([{ x: 2 }, { x: 1 }], [{ x: 1 }], (v) => v.x); // [2]
```
