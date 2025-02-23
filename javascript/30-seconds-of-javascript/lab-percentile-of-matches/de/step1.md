# Berechnung des Percentils von Übereinstimmungen

Um das Percentil von Übereinstimmungen im untenstehenden angegebenen Array kleiner oder gleich einem angegebenen Wert zu berechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um die Code-Praxis zu starten.
2. Verwenden Sie die `Array.prototype.reduce()`-Methode, um die Anzahl der Werte unterhalb des angegebenen Werts und die Anzahl der Werte, die gleich dem angegebenen Wert sind, zu berechnen.
3. Wenden Sie die Percentilformel an, um den Prozentsatz der Übereinstimmungen zu erhalten.
4. Hier ist ein Beispiel-Codeausschnitt:

```js
const percentile = (arr, val) =>
  (100 *
    arr.reduce(
      (acc, v) => acc + (v < val ? 1 : 0) + (v === val ? 0.5 : 0),
      0
    )) /
  arr.length;
```

5. Um die Funktion zu testen, verwenden Sie diesen Beispielcode:

```js
percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6); // Ausgabe: 55
```

Diese Funktion gibt den Prozentsatz der Übereinstimmungen im angegebenen Array aus, die kleiner oder gleich dem angegebenen Wert sind.
