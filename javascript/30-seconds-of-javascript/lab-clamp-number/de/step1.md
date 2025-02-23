# Funktion zum Einschränken einer Zahl innerhalb eines Bereichs

Um eine Zahl innerhalb eines bestimmten Bereichs einzuschränken, verwenden Sie die `clampNumber`-Funktion.

Beginnen Sie zunächst, indem Sie die Konsole/SSH öffnen und `node` eingeben, um zu üben.

Die `clampNumber`-Funktion nimmt drei Parameter entgegen: `num`, `a` und `b`. Sie schränkt `num` innerhalb des von den Grenzwerten `a` und `b` definierten eingeschlossenen Bereichs ein und gibt das Ergebnis zurück.

Wenn `num` innerhalb des Bereichs liegt, gibt die Funktion `num` zurück. Andernfalls gibt sie die nächstliegende Zahl im Bereich zurück.

Hier ist der Code für die `clampNumber`-Funktion:

```js
const clampNumber = (num, a, b) =>
  Math.max(Math.min(num, Math.max(a, b)), Math.min(a, b));
```

Und hier sind einige Beispiele für die Verwendung der Funktion:

```js
clampNumber(2, 3, 5); // 3
clampNumber(1, -1, -5); // -1
```
