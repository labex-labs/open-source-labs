# Wie man das längste Element in einem Array findet

Um das längste Element in einem Array zu finden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Die Funktion nimmt beliebig viele iterierbare Objekte oder Objekte mit einer `length`-Eigenschaft entgegen und gibt das längste zurück. Sie verwendet `Array.prototype.reduce()`, um die Länge von Objekten zu vergleichen und das längste zu finden. Wenn mehrere Objekte die gleiche Länge haben, gibt die Funktion das erste zurück. Wenn keine Argumente übergeben werden, gibt sie `undefined` zurück.

Hier ist der Code:

```js
const longestItem = (...vals) =>
  vals.reduce((a, x) => (x.length > a.length ? x : a));
```

Sie können die Funktion wie folgt verwenden:

```js
longestItem("this", "is", "a", "testcase"); // 'testcase'
longestItem(...["a", "ab", "abc"]); // 'abc'
longestItem(...["a", "ab", "abc"], "abcd"); // 'abcd'
longestItem([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]); // [1, 2, 3, 4, 5]
longestItem([1, 2, 3], "foobar"); // 'foobar'
```
