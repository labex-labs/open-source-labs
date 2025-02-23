# Funktion zum Initialisieren eines Arrays mit einem Bereich

Um ein Array mit einem Bereich von Zahlen zu initialisieren, verwenden Sie die folgende Funktion:

```js
const initializeArrayWithRange = (end, start = 0, step = 1) => {
  const length = Math.ceil((end - start + 1) / step);
  return Array.from({ length }, (_, i) => i * step + start);
};
```

Diese Funktion nimmt drei Argumente entgegen: `end` (erforderlich), `start` (optional, Standardwert ist `0`) und `step` (optional, Standardwert ist `1`). Sie gibt ein Array zurück, das die Zahlen im angegebenen Bereich enthält, wobei `start` und `end` inklusive sind mit ihrer gemeinsamen Differenz `step`.

Um diese Funktion zu verwenden, rufen Sie sie einfach mit den gewünschten Bereichsparametern auf:

```js
initializeArrayWithRange(5); // [0, 1, 2, 3, 4, 5]
initializeArrayWithRange(7, 3); // [3, 4, 5, 6, 7]
initializeArrayWithRange(9, 0, 2); // [0, 2, 4, 6, 8]
```

Diese Funktion verwendet `Array.from()`, um ein Array der gewünschten Länge zu erstellen, und dann eine Map-Funktion, um das Array mit den gewünschten Werten im angegebenen Bereich zu füllen. Wenn Sie das zweite Argument, `start`, weglassen, wird ein Standardwert von `0` verwendet. Wenn Sie das letzte Argument, `step`, weglassen, wird ein Standardwert von `1` verwendet.
