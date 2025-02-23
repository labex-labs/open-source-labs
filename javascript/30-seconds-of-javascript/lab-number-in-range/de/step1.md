# Funktion zum Überprüfen, ob eine Zahl innerhalb eines angegebenen Bereichs liegt

Um zu überprüfen, ob eine Zahl innerhalb eines bestimmten Bereichs liegt, verwenden Sie die `inRange`-Funktion. Öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein, um zu beginnen, zu codieren.

Hier sind die Schritte zum Verwenden der `inRange`-Funktion:

1. Verwenden Sie arithmetische Vergleiche, um zu überprüfen, ob die gegebene Zahl im angegebenen Bereich liegt.
2. Wenn das zweite Argument, `end`, nicht angegeben ist, wird der Bereich als von `0` bis `start` betrachtet.
3. Die `inRange`-Funktion nimmt drei Argumente: `n`, `start` und `end`.
4. Wenn `end` kleiner als `start` ist, tauscht die Funktion die Werte von `start` und `end` aus.
5. Wenn `end` nicht angegeben ist, überprüft die Funktion, ob `n` größer oder gleich `0` und kleiner als `start` ist.
6. Wenn `end` angegeben ist, überprüft die Funktion, ob `n` größer oder gleich `start` und kleiner als `end` ist.
7. Die Funktion gibt `true` zurück, wenn `n` innerhalb des angegebenen Bereichs liegt, und `false` andernfalls.

Hier ist die `inRange`-Funktion:

```js
const inRange = (n, start, end = null) => {
  if (end && start > end) [end, start] = [start, end];
  return end == null ? n >= 0 && n < start : n >= start && n < end;
};
```

Hier sind einige Beispiele für die Verwendung der `inRange`-Funktion:

```js
inRange(3, 2, 5); // true
inRange(3, 4); // true
inRange(2, 3, 5); // false
inRange(3, 2); // false
```
