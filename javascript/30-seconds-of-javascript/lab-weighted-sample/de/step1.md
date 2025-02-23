# Wie man eine gewichtete Stichprobe aus einem Array in JavaScript bekommt

Um zufällig ein Element aus einem Array basierend auf den bereitgestellten Gewichten zu erhalten, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()`, um ein Array von Teilsummen für jedes Element in `weights` zu erstellen.
3. Verwenden Sie `Math.random()`, um eine Zufallszahl zu generieren, und `Array.prototype.findIndex()`, um den richtigen Index basierend auf dem zuvor erzeugten Array zu finden.
4. Geben Sie schließlich das Element von `arr` mit dem erzeugten Index zurück.

Hier ist der Code, um dies zu erreichen:

```js
const weightedSample = (arr, weights) => {
  let roll = Math.random();
  return arr[
    weights
      .reduce(
        (acc, w, i) => (i === 0 ? [w] : [...acc, acc[acc.length - 1] + w]),
        []
      )
      .findIndex((v, i, s) => roll >= (i === 0 ? 0 : s[i - 1]) && roll < v)
  ];
};
```

Sie können diese Funktion testen, indem Sie ein Array und seine entsprechenden Gewichte als Argumente übergeben:

```js
weightedSample([3, 7, 9, 11], [0.1, 0.2, 0.6, 0.1]); // 9
```
