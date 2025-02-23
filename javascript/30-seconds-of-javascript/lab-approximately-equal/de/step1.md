# Prüfen auf annähernde Gleichheit von Zahlen in JavaScript

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Dieser Code prüft, ob zwei Zahlen ungefähr gleich zueinander sind. Dazu tun Sie Folgendes:

- Verwenden Sie die `Math.abs()`-Methode, um die absolute Differenz der beiden Werte mit `epsilon` zu vergleichen.
- Wenn Sie keinen dritten Argument, `epsilon`, angeben, verwendet die Funktion einen Standardwert von `0.001`.

Hier ist der Code:

```js
const approximatelyEqual = (v1, v2, epsilon = 0.001) =>
  Math.abs(v1 - v2) < epsilon;
```

Um die Funktion zu testen, können Sie sie mit zwei Zahlen als Argumente aufrufen, wie folgt:

```js
approximatelyEqual(Math.PI / 2.0, 1.5708); // true
```

Dies wird `true` zurückgeben, da `Math.PI / 2.0` mit einem Epsilon von `0.001` ungefähr gleich `1.5708` ist.
