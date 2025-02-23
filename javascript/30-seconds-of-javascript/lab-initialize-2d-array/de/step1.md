# Initialisieren eines 2D-Arrays in JavaScript

Um in JavaScript ein 2D-Array zu initialisieren, kannst du folgenden Code verwenden:

```js
const initialize2DArray = (width, height, value = null) => {
  return Array.from({ length: height }).map(() =>
    Array.from({ length: width }).fill(value)
  );
};
```

Dieser Code verwendet `Array.from()` und `Array.prototype.map()`, um ein Array mit `height` Zeilen zu erstellen, wobei jede Zeile ein neues Array der Länge `width` ist. Außerdem verwendet er `Array.prototype.fill()`, um alle Elemente im Array auf den `value`-Parameter zu setzen. Wenn kein `value` angegeben wird, standardmäßig auf `null`.

Du kannst die Funktion wie folgt aufrufen:

```js
initialize2DArray(2, 2, 0); // [[0, 0], [0, 0]]
```

Dies erstellt ein 2D-Array mit einer Breite von 2, einer Höhe von 2 und allen Werten auf 0 gesetzt.
