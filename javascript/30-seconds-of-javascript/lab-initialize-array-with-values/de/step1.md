# Funktion zum Initialisieren eines Arrays mit bestimmten Werten

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion initialisiert ein Array mit den angegebenen Werten:

- Verwenden Sie den `Array()`-Konstruktor, um ein Array der gewünschten Länge zu erstellen.
- Verwenden Sie `Array.prototype.fill()`, um es mit den gewünschten Werten zu füllen.
- Wenn kein Wert angegeben ist, standardmäßig `0`.

```js
const initializeArrayWithValues = (length, value = 0) =>
  Array(length).fill(value);
```

Beispielverwendung:

```js
initializeArrayWithValues(5, 2); // [2, 2, 2, 2, 2]
```
