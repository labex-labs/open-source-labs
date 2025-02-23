# Array von sukzessiven Werten

Um in JavaScript ein Array von sukzessiven Werten zu erstellen, können Sie die `Array.prototype.reduce()`-Methode verwenden. Diese Methode wendet eine Funktion auf einen Akkumulator und jedes Element im Array von links nach rechts an und gibt ein Array der sukzessiv reduzierten Werte zurück.

Hier ist, wie die `reduceSuccessive`-Funktion verwendet wird, um die gegebene Funktion auf das gegebene Array anzuwenden und jedes neue Ergebnis zu speichern:

```js
const reduceSuccessive = (arr, fn, acc) =>
  arr.reduce(
    (res, val, i, arr) => (res.push(fn(res.slice(-1)[0], val, i, arr)), res),
    [acc]
  );
```

Anschließend können Sie die `reduceSuccessive`-Funktion mit einem Array, einer Funktion und einem Anfangswert für den Akkumulator aufrufen:

```js
reduceSuccessive([1, 2, 3, 4, 5, 6], (acc, val) => acc + val, 0);
// [0, 1, 3, 6, 10, 15, 21]
```

Um mit dieser Funktion zu beginnen, die Codierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
