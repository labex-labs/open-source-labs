# Anweisungen zum Finden der Schnittmenge von abgebildeten Arrays

Um gemeinsame Elemente in zwei Arrays zu finden, nachdem eine Funktion auf jedes Element beider Arrays angewendet wurde, folgen Sie diesen Schritten:

1. Öffnen Sie die Konsole/SSH und geben Sie `node` ein.
2. Verwenden Sie den unten bereitgestellten Code:

```js
const intersectionBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return [...new Set(a)].filter((x) => s.has(fn(x)));
};
```

3. Ersetzen Sie in Ihrem Code `a` und `b` durch Ihre Arrays und `fn` durch die Funktion, die Sie auf jedes Element anwenden möchten.
4. Führen Sie den Code aus, um das resultierende Array mit gemeinsamen Elementen zu erhalten.

Beispiel:

```js
intersectionBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [2.1]
intersectionBy(
  [{ title: "Apple" }, { title: "Orange" }],
  [{ title: "Orange" }, { title: "Melon" }],
  (x) => x.title
); // [{ title: 'Orange' }]
```

Im ersten Beispiel wird die Funktion `Math.floor` auf die Arrays `[2.1, 1.2]` und `[2.3, 3.4]` angewendet, was das gemeinsame Element `[2.1]` zurückgibt.
Im zweiten Beispiel wird die Funktion `x => x.title` auf die Arrays `[{ title: 'Apple' }, { title: 'Orange' }]` und `[{ title: 'Orange' }, { title: 'Melon' }]` angewendet, was das gemeinsame Element `[{ title: 'Orange' }]` zurückgibt.
