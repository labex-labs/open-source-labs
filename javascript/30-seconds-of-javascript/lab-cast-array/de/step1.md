# Werte in JavaScript in Arrays umwandeln

Um einen Wert in ein Array umzuwandeln, verwenden Sie die unten bereitgestellte `castArray`-Funktion.

```js
const castArray = (val) => (Array.isArray(val) ? val : [val]);
```

Um diese Funktion zu verwenden, übergeben Sie als Argument den Wert, den Sie umwandeln möchten. Die Funktion prüft mithilfe von `Array.isArray()`, ob der Wert bereits ein Array ist. Ist es ein Array, wird die Funktion es unverändert zurückgeben. Ist es kein Array, wird die Funktion den Wert in einem Array eingeschlossen zurückgeben.

Hier ist ein Beispiel dafür, wie `castArray` verwendet wird:

```js
castArray("foo"); // gibt zurück: ['foo']
castArray([1]); // gibt zurück: [1]
```

Um zu beginnen, JavaScript zu programmieren, öffnen Sie das Terminal oder SSH und geben Sie `node` ein.
