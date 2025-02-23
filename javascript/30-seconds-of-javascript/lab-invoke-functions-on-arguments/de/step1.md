# Funktionen auf Argumenten aufrufen

Um Code mit Node.js auszuführen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Um eine Funktion zu erstellen, die jede bereitgestellte Funktion mit den Argumenten aufruft, die sie erhält, und die Ergebnisse zurückgibt:

- Verwenden Sie `Array.prototype.map()` und `Function.prototype.apply()`, um jede Funktion auf die angegebenen Argumente anzuwenden.

```js
const over =
  (...fns) =>
  (...args) =>
    fns.map((fn) => fn.apply(null, args));
```

Beispiel:

```js
const minMax = over(Math.min, Math.max);
minMax(1, 2, 3, 4, 5); // [1, 5]
```
