# JavaScript-Funktion zum Gruppieren von Array-Elementen

Um Elemente in Arrays zu gruppieren, kannst du die `zipWith`-Funktion verwenden.

So funktioniert es:

- Die Funktion nimmt eine unbegrenzte Anzahl von Arrays als Argumente entgegen.
- Sie überprüft, ob das letzte Argument eine Funktion ist.
- Sie verwendet `Math.max()`, um die Länge des längsten Arrays zu ermitteln.
- Sie erstellt ein neues Array von gruppierten Elementen mit `Array.from()` und einer Mapping-Funktion.
- Wenn die Längen der Argument-Arrays unterschiedlich sind, wird `undefined` verwendet, wo kein Wert gefunden werden konnte.
- Die Funktion wird mit den Elementen jeder Gruppe aufgerufen.

Hier ist ein Beispiel für die Verwendung der `zipWith`-Funktion:

```js
zipWith([1, 2], [10, 20], [100, 200], (a, b, c) => a + b + c); // [111, 222]
zipWith(
  [1, 2, 3],
  [10, 20],
  [100, 200],
  (a, b, c) =>
    (a != null ? a : "a") + (b != null ? b : "b") + (c != null ? c : "c")
); // [111, 222, '3bc']
```

Um die `zipWith`-Funktion zu verwenden, öffne das Terminal/SSH und tippe `node`.
