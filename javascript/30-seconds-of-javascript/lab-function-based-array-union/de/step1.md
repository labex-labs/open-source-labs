# Wie man die Vereinigung zweier Arrays basierend auf einer Funktion findet

Um die Vereinigung zweier Arrays basierend auf einer Funktion mit Node.js zu finden, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein.
2. Verwenden Sie den folgenden Code, um eine `Set` mit allen Werten von `a` und Werten in `b` zu erstellen, für die der Vergleichsoperator in `a` keine Übereinstimmungen findet, indem Sie `Array.prototype.findIndex()` verwenden:

```js
const unionWith = (a, b, comp) =>
  Array.from(
    new Set([...a, ...b.filter((x) => a.findIndex((y) => comp(x, y)) === -1)])
  );
```

3. Rufen Sie die `unionWith`-Funktion mit drei Argumenten auf: das erste Array, das zweite Array und die Vergleichsfunktion.
4. Die Funktion gibt jedes Element zurück, das in mindestens einem der beiden Arrays mindestens einmal vorhanden ist, unter Verwendung der bereitgestellten Vergleichsfunktion.
5. Hier ist ein Beispiel für das Aufrufen der `unionWith`-Funktion:

```js
unionWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
);
// [1, 1.2, 1.5, 3, 0, 3.9]
```

Dies wird `[1, 1.2, 1.5, 3, 0, 3.9]` als die Vereinigung der beiden Arrays zurückgeben.
