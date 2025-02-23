# Generator, der Werte produziert, solange eine Bedingung wahr ist

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Dies erstellt einen Generator, der solange neue Werte produziert, wie die gegebene Bedingung erfüllt ist.

Der Generator wird mit einem `Startwert` initialisiert, der verwendet wird, um den aktuellen `Wert` zu initialisieren. Eine `while-Schleife` wird dann verwendet, um zu iterieren, solange die `Bedingungsfunktion`, die mit dem aktuellen `Wert` aufgerufen wird, `true` zurückgibt.

Das `yield`-Schlüsselwort wird verwendet, um den aktuellen `Wert` zurückzugeben und optional einen neuen Startwert, `nextSeed`, zu empfangen. Die `next`-Funktion wird verwendet, um den nächsten Wert aus dem aktuellen `Wert` und dem `nextSeed` zu berechnen.

```js
const generateWhile = function* (seed, condition, next) {
  let val = seed;
  let nextSeed = null;
  while (condition(val)) {
    nextSeed = yield val;
    val = next(val, nextSeed);
  }
  return val;
};
```

Um den Generator zu verwenden, rufen Sie ihn mit den `Startwert`, `Bedingungsfunktion` und `next`-Funktionen auf. Beispielsweise wird `[...generateWhile(1, v => v <= 5, v => ++v)]` `[1, 2, 3, 4, 5]` zurückgeben.
