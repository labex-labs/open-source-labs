# Funktion zur Berechnung der Summe der Potenzen in einem angegebenen Bereich

Um die Summe der Potenzen aller Zahlen innerhalb eines bestimmten Bereichs (einschließlich der Endpunkte) zu berechnen, verwenden Sie die folgende Funktion:

```js
const sumPower = (end, power = 2, start = 1) =>
  Array(end + 1 - start)
    .fill(0)
    .map((x, i) => (i + start) ** power)
    .reduce((a, b) => a + b, 0);
```

So können Sie diese Funktion verwenden:

- Rufen Sie `sumPower(end)` auf, um die Summe der Quadrate aller Zahlen von 1 bis `end` zu berechnen.
- Rufen Sie `sumPower(end, power)` auf, um die Summe der `power`-ten Potenzen aller Zahlen von 1 bis `end` zu berechnen.
- Rufen Sie `sumPower(end, power, start)` auf, um die Summe der `power`-ten Potenzen aller Zahlen von `start` bis `end` zu berechnen.

Beachten Sie, dass die zweiten und dritten Argumente (`power` und `start`) optional sind und standardmäßig auf `2` und `1` festgelegt sind, wenn nicht angegeben.

Beispiel:

```js
sumPower(10); // Gibt 385 zurück (Summe der Quadrate der Zahlen von 1 bis 10)
sumPower(10, 3); // Gibt 3025 zurück (Summe der Kuben der Zahlen von 1 bis 10)
sumPower(10, 3, 5); // Gibt 2925 zurück (Summe der Kuben der Zahlen von 5 bis 10)
```
