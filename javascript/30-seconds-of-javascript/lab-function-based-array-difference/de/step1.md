# Wie man Werte aus einem Array anhand einer Funktion herausfiltert

Um alle Werte aus einem Array anhand einer gegebenen Vergleichsfunktion herauszufiltern, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie `Array.prototype.filter()` und `Array.prototype.findIndex()`, um die passenden Werte zu finden.
3. Lassen Sie das letzte Argument, `comp`, weg, um einen standardmäßigen strikt-Äquivalenz-Vergleichsoperator zu verwenden.
4. Verwenden Sie folgenden Code:

```js
const differenceWith = (arr, val, comp = (a, b) => a === b) =>
  arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1);
```

5. Testen Sie Ihre Funktion mit folgenden Beispielen:

```js
differenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0],
  (a, b) => Math.round(a) === Math.round(b)
); // Erwartetes Ergebnis: [1, 1.2]

differenceWith([1, 1.2, 1.3], [1, 1.3, 1.5]); // Erwartetes Ergebnis: [1.2]
```
