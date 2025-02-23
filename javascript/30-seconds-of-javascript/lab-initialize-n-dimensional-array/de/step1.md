# Wie man ein n-dimensionales Array in JavaScript initialisiert

Um ein n-dimensionales Array in JavaScript zu erstellen, kannst du die Funktion `initializeNDArray` verwenden. Diese Funktion nimmt einen Wert und beliebig viele Dimensionen als Argumente entgegen und gibt ein neues Array zurück, das mit diesem Wert initialisiert ist.

Um `initializeNDArray` zu verwenden, kannst du die folgenden Schritte ausführen:

1. Öffne das Terminal/SSH und tippe `node`, um zu beginnen zu codieren.
2. Verwende Rekursion, um das Array mit der angegebenen Anzahl von Dimensionen zu erstellen.
3. Verwende `Array.from()` und `Array.prototype.map()`, um Zeilen zu generieren, wobei jede Zeile ein neues Array ist, das mit `initializeNDArray()` initialisiert wird.

Hier ist der Code für die Funktion `initializeNDArray`:

```js
const initializeNDArray = (val, ...args) =>
  args.length === 0
    ? val
    : Array.from({ length: args[0] }).map(() =>
        initializeNDArray(val, ...args.slice(1))
      );
```

Anschließend kannst du `initializeNDArray` mit dem gewünschten Wert und der Anzahl der Dimensionen aufrufen. Beispielsweise:

```js
initializeNDArray(1, 3); // [1, 1, 1]
initializeNDArray(5, 2, 2, 2); // [[[5, 5], [5, 5]], [[5, 5], [5, 5]]]
```
