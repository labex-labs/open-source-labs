# Array-Elemente gruppieren

Um die Elemente von Arrays anhand ihrer Position in den ursprünglichen Arrays zu gruppieren, verwenden Sie die unten bereitgestellte `zip`-Funktion.

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Die `zip`-Funktion verwendet `Math.max()` und `Function.prototype.apply()`, um das längste Array in den Argumenten zu erhalten.
- Sie erstellt ein Array mit dieser Länge als Rückgabewert und verwendet `Array.from()` mit einer Mapping-Funktion, um ein Array von gruppierten Elementen zu erstellen.
- Wenn die Längen der Argument-Arrays unterschiedlich sind, wird `undefined` verwendet, wenn kein Wert gefunden werden kann.

```js
const zip = (...arrays) => {
  const maxLength = Math.max(...arrays.map((x) => x.length));
  return Array.from({ length: maxLength }).map((_, i) => {
    return Array.from({ length: arrays.length }, (_, k) => arrays[k][i]);
  });
};
```

Beispielverwendung:

```js
zip(["a", "b"], [1, 2], [true, false]); // [['a', 1, true], ['b', 2, false]]
zip(["a"], [1, 2], [true, false]); // [['a', 1, true], [undefined, 2, false]]
```
