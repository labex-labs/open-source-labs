# Hamming-Distanz-Berechnung

Um die Hamming-Distanz zwischen zwei Werten zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codierung zu beginnen.
2. Verwenden Sie den XOR-Operator (`^`), um die Bitunterschiede zwischen den beiden Zahlen zu finden.
3. Konvertieren Sie das Ergebnis in einen Binärstring mit `Number.prototype.toString()`.
4. Zählen Sie die Anzahl der `1` im String mit `String.prototype.match()`.
5. Geben Sie die Anzahl zurück.

Hier ist der Code für die `hammingDistance`-Funktion:

```js
const hammingDistance = (num1, num2) =>
  ((num1 ^ num2).toString(2).match(/1/g) || "").length;
```

Sie können die Funktion testen, indem Sie `hammingDistance(2, 3); // 1` ausführen.
