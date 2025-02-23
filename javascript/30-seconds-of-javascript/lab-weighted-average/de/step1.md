# Wie man das gewichtete Mittel in JavaScript berechnet

Um das gewichtete Mittel von zwei oder mehr Zahlen in JavaScript zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()`, um die gewichtete Summe der Werte und die Summe der Gewichte zu berechnen.
3. Teilen Sie die gewichtete Summe der Werte durch die Summe der Gewichte, um das gewichtete Mittel zu erhalten.

Hier ist der JavaScript-Code für die `weightedAverage`-Funktion:

```js
const weightedAverage = (nums, weights) => {
  const [sum, weightSum] = weights.reduce(
    (acc, w, i) => {
      acc[0] = acc[0] + nums[i] * w;
      acc[1] = acc[1] + w;
      return acc;
    },
    [0, 0]
  );
  return sum / weightSum;
};
```

Sie können die `weightedAverage`-Funktion verwenden, um das gewichtete Mittel eines Arrays von Zahlen und eines Arrays von Gewichten wie folgt zu berechnen:

```js
weightedAverage([1, 2, 3], [0.6, 0.2, 0.3]); // 1.72727
```
