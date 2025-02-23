# Levenshtein-Distanz-Algorithmus

Um die Differenz zwischen zwei Zeichenketten zu berechnen, kannst du den Levenshtein-Distanz-Algorithmus verwenden. Hier ist, wie du es tun kannst:

1. Wenn eine der beiden Zeichenketten eine `length` von null hat, gib die `length` der anderen zurück.
2. Verwende eine geschachtelte `for-Schleife`, um über die Buchstaben der Ziel- und Quellzeichenkette zu iterieren.
3. Berechne die Kosten für die Substitution der jeweils `i - 1` und `j - 1` entsprechenden Buchstaben in der Ziel- und Quellzeichenkette (`0`, wenn sie gleich sind, `1` andernfalls).
4. Verwende `Math.min()`, um jedes Element im 2D-Array mit dem Minimum der Zelle darüber um eins erhöht, der Zelle links um eins erhöht oder der Zelle in der oberen linken Ecke um die zuvor berechnete Kosten zu füllen.
5. Gib das letzte Element der letzten Zeile des erzeugten Arrays zurück.

Um mit diesem Coding zu üben, öffne das Terminal/SSH und tippe `node`. Hier ist der Code, den du verwenden kannst:

```js
const levenshteinDistance = (s, t) => {
  if (!s.length) return t.length;
  if (!t.length) return s.length;
  const arr = [];
  for (let i = 0; i <= t.length; i++) {
    arr[i] = [i];
    for (let j = 1; j <= s.length; j++) {
      arr[i][j] =
        i === 0
          ? j
          : Math.min(
              arr[i - 1][j] + 1,
              arr[i][j - 1] + 1,
              arr[i - 1][j - 1] + (s[j - 1] === t[i - 1] ? 0 : 1)
            );
    }
  }
  return arr[t.length][s.length];
};

console.log(levenshteinDistance("duck", "dark")); // 2
```
