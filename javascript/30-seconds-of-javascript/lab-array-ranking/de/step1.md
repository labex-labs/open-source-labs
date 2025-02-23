# Arrays bewerten

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Diese Funktion berechnet die Bewertung eines Arrays basierend auf einer Vergleichsfunktion.

Um diese Funktion zu verwenden, können Sie Folgendes tun:

- Verwenden Sie `Array.prototype.map()` und `Array.prototype.filter()`, um jedes Element mithilfe der bereitgestellten Vergleichsfunktion zu einer Rangfolge zuzuordnen.

Hier ist ein Beispiel für die Verwendung:

```js
const ranking = (arr, compFn) =>
  arr.map((a) => arr.filter((b) => compFn(a, b)).length + 1);
```

Beispiel:

```js
ranking([8, 6, 9, 5], (a, b) => a < b);
// [2, 3, 1, 4]
ranking(["c", "a", "b", "d"], (a, b) => a.localeCompare(b) > 0);
// [3, 1, 2, 4]
```
