# Funktion zum Kombinieren von Objekt-Arrays basierend auf einem bestimmten Schlüssel

Um zwei Objekt-Arrays basierend auf einem bestimmten Schlüssel zu kombinieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()` mit einem Objekt-Akkumulator, um alle Objekte in beiden Arrays basierend auf der angegebenen `prop` zu kombinieren.
3. Verwenden Sie `Object.values()`, um das resultierende Objekt in ein Array zu konvertieren und zurückzugeben.

Hier ist die Funktion, die Sie verwenden können:

```js
const combine = (a, b, prop) =>
  Object.values(
    [...a, ...b].reduce((acc, v) => {
      if (v[prop])
        acc[v[prop]] = acc[v[prop]] ? { ...acc[v[prop]], ...v } : { ...v };
      return acc;
    }, {})
  );
```

Hier ist ein Beispiel, wie diese Funktion verwendet werden kann:

```js
const x = [
  { id: 1, name: "John" },
  { id: 2, name: "Maria" }
];
const y = [{ id: 1, age: 28 }, { id: 3, age: 26 }, { age: 3 }];
combine(x, y, "id");
// [
//  { id: 1, name: 'John', age: 28 },
//  { id: 2, name: 'Maria' },
//  { id: 3, age: 26 }
// ]
```
