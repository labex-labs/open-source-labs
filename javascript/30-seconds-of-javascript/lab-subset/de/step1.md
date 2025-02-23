# Überprüfen, ob eine Teilmenge eines Iterablen in einem anderen Iterablen enthalten ist

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Diese Funktion überprüft, ob das erste Iterable eine Teilmenge des zweiten Iterablen ist, wobei doppelte Werte ausgeschlossen werden.

Um dies zu erreichen, können Sie Folgendes tun:

- Erstellen Sie aus jedem Iterable ein neues `Set`-Objekt, indem Sie den `Set`-Konstruktor verwenden.
- Verwenden Sie `Array.prototype.every()` und `Set.prototype.has()`, um zu überprüfen, ob jeder Wert im ersten Iterable im zweiten Iterable enthalten ist.

Hier ist eine Beispielimplementierung:

```js
const subSet = (a, b) => {
  const setA = new Set(a);
  const setB = new Set(b);
  return [...setA].every((value) => setB.has(value));
};
```

Sie können die `subSet`-Funktion verwenden, indem Sie zwei Sets übergeben, um sie zu vergleichen. Beispielsweise:

```js
subSet(new Set([1, 2]), new Set([1, 2, 3, 4])); // true
subSet(new Set([1, 5]), new Set([1, 2, 3, 4])); // false
```
