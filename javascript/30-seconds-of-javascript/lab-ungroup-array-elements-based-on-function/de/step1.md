# Wie man Array-Elemente basierend auf einer Funktion aufspaltet

Wenn Sie die Elemente in einem von `zip` erzeugten Array aufspalten und eine Funktion anwenden müssen, können Sie `unzipWith` verwenden. Hier ist, wie Sie es implementieren können:

1. Verwenden Sie `Math.max()` und den Spread-Operator (`...`), um das längste Unterarray im Array zu erhalten, und `Array.prototype.map()`, um jedes Element zu einem Array zu machen.
2. Verwenden Sie `Array.prototype.reduce()` und `Array.prototype.forEach()`, um gruppierte Werte auf einzelne Arrays zuzuordnen.
3. Verwenden Sie `Array.prototype.map()` und den Spread-Operator (`...`), um `fn` auf jede einzelne Gruppe von Elementen anzuwenden.

```js
const unzipWith = (arr, fn) =>
  arr
    .reduce(
      (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
      Array.from({
        length: Math.max(...arr.map((x) => x.length))
      }).map((x) => [])
    )
    .map((val) => fn(...val));
```

Um `unzipWith` zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Anschließend können Sie das folgende Beispiel ausführen:

```js
unzipWith(
  [
    [1, 10, 100],
    [2, 20, 200]
  ],
  (...args) => args.reduce((acc, v) => acc + v, 0)
);
// [3, 30, 300]
```

Dies wird ein Array von Elementen erzeugen, indem die Elemente im von `zip` erzeugten Eingabearray aufgespalten und die bereitgestellte Funktion angewendet wird.
