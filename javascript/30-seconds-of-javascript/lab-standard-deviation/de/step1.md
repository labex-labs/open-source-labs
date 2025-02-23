# Standardabweichung

Um die Standardabweichung eines Arrays von Zahlen in JavaScript zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die unten bereitgestellte Funktion `standardDeviation(arr, usePopulation = false)`.
3. Übergeben Sie ein Array von Zahlen als erstes Argument an die Funktion.
4. Lassen Sie das zweite Argument `usePopulation` weg, um die Stichprobenstandardabweichung zu erhalten. Legen Sie es auf `true` fest, um die Populationsstandardabweichung zu erhalten.

```js
const standardDeviation = (arr, usePopulation = false) => {
  const mean = arr.reduce((acc, val) => acc + val, 0) / arr.length;
  return Math.sqrt(
    arr
      .reduce((acc, val) => acc.concat((val - mean) ** 2), [])
      .reduce((acc, val) => acc + val, 0) /
      (arr.length - (usePopulation ? 0 : 1))
  );
};
```

Beispielverwendung:

```js
standardDeviation([10, 2, 38, 23, 38, 23, 21]); // 13.284434142114991 (Stichprobe)
standardDeviation([10, 2, 38, 23, 38, 23, 21], true); // 12.29899614287479 (Population)
```
