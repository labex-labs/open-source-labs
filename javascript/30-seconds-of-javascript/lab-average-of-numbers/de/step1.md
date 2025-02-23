# Wie man den Durchschnitt von Zahlen in JavaScript berechnet

Um den Durchschnitt von zwei oder mehr Zahlen in JavaScript zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie die integrierte `Array.prototype.reduce()`-Methode, um jeden Wert einem Akkumulator hinzuzufügen, der mit einem Wert von `0` initialisiert wird.
3. Teilen Sie die resultierende Summe durch die Länge des Arrays.

Hier ist ein Beispiel-Codeausschnitt, den Sie verwenden können:

```js
const average = (...nums) =>
  nums.reduce((acc, val) => acc + val, 0) / nums.length;
```

Sie können die `average`-Funktion mit einem Array oder mehreren Argumenten aufrufen:

```js
average(...[1, 2, 3]); // 2
average(1, 2, 3); // 2
```
