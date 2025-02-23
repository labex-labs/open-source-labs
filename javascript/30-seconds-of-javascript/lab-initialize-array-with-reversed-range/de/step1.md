# Wie man ein Array mit umgekehrtem Bereich in JavaScript initialisiert

Um ein Array mit einem umgekehrten Bereich in JavaScript zu initialisieren, verwenden Sie die folgende Funktion:

```js
const initializeArrayWithRangeRight = (end, start = 0, step = 1) =>
  Array.from({ length: Math.ceil((end + 1 - start) / step) }).map(
    (v, i, arr) => (arr.length - i - 1) * step + start
  );
```

Diese Funktion erstellt ein Array, das die Zahlen im angegebenen Bereich in umgekehrter Reihenfolge enthält. Die `start`- und `end`-Parameter sind inklusiv, und der `step`-Parameter gibt die gemeinsame Differenz zwischen den Zahlen im Bereich an.

Um die Funktion zu verwenden, rufen Sie sie mit den gewünschten `end`-, `start`- und `step`-Werten als Argumente auf, wie folgt:

```js
initializeArrayWithRangeRight(5); // [5, 4, 3, 2, 1, 0]
initializeArrayWithRangeRight(7, 3); // [7, 6, 5, 4, 3]
initializeArrayWithRangeRight(9, 0, 2); // [8, 6, 4, 2, 0]
```

Wenn Sie das `start`-Argument weglassen, standardmäßig auf `0`. Wenn Sie das `step`-Argument weglassen, standardmäßig auf `1`.
