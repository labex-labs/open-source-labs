# Wie man in JavaScript Arrayelemente aufspaltet

Um die Elemente in einem Array, das von der `zip`-Funktion erzeugt wurde, aufzuspalten, kann man ein Array von Arrays mit der `unzip`-Funktion in JavaScript erstellen. Hier ist wie:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Math.max()`, `Function.prototype.apply()`, um das längste Unterarray im Array zu erhalten, und `Array.prototype.map()`, um jedes Element zu einem Array zu machen.
3. Verwenden Sie `Array.prototype.reduce()` und `Array.prototype.forEach()`, um gruppierte Werte auf einzelne Arrays zuzuordnen.

Hier ist der Code für die `unzip`-Funktion:

```js
const unzip = (arr) =>
  arr.reduce(
    (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
    Array.from({
      length: Math.max(...arr.map((x) => x.length))
    }).map((x) => [])
  );
```

Sie können die `unzip`-Funktion mit den folgenden Beispielen verwenden:

```js
unzip([
  ["a", 1, true],
  ["b", 2, false]
]); // [['a', 'b'], [1, 2], [true, false]]
unzip([
  ["a", 1, true],
  ["b", 2]
]); // [['a', 'b'], [1, 2], [true]]
```

Indem Sie diese Schritte befolgen, können Sie in JavaScript leicht Arrayelemente aufspalten.
