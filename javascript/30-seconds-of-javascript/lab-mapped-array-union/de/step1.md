# Funktion zum Vereinigen von Arrays mit einer angegebenen Zuordnungsfunktion

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion gibt ein Array von Elementen zurück, die in einem der beiden Eingabe-Arrays vorhanden sind, nachdem die angegebene Zuordnungsfunktion auf jedes Element in beiden Arrays angewendet wurde.

Hier sind die Schritte, um dies zu erreichen:

1. Erstellen Sie eine neue `Set`, indem Sie die Zuordnungsfunktion auf alle Werte im ersten Eingabe-Array `a` anwenden.
2. Erstellen Sie eine weitere `Set`, die aus allen Elementen in `b` besteht, die nicht mit irgendwelchen Werten in der zuvor erstellten `Set` übereinstimmen, wenn die Zuordnungsfunktion angewendet wird.
3. Vereinigen Sie die beiden Mengen und konvertieren Sie sie zu einem Array.
4. Geben Sie das resultierende Array zurück.

Hier ist der Code für die `unionBy`-Funktion:

```js
const unionBy = (a, b, fn) => {
  const setA = new Set(a.map(fn));
  return Array.from(new Set([...a, ...b.filter((x) => !setA.has(fn(x)))]));
};
```

Hier sind einige Beispiele für die Verwendung der `unionBy`-Funktion:

```js
unionBy([2.1], [1.2, 2.3], Math.floor); // Ausgabe: [2.1, 1.2]
unionBy([{ id: 1 }, { id: 2 }], [{ id: 2 }, { id: 3 }], (x) => x.id);
// Ausgabe: [{ id: 1 }, { id: 2 }, { id: 3 }]
```
