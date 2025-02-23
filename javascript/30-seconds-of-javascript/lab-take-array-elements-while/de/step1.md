# Entfernen von Array-Elementen basierend auf einer Bedingung

Um Elemente in einem Array basierend auf einer Bedingung zu entfernen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die `takeWhile`-Funktion entfernt Elemente in einem Array, bis die übergebene Funktion `false` zurückgibt, und gibt dann die entfernten Elemente zurück.

Hier sind die Schritte, um die `takeWhile`-Funktion zu verwenden:

- Iterieren Sie über das Array mit einer `for...of`-Schleife über `Array.prototype.entries()`.
- Iterieren Sie, bis der zurückgegebene Wert der Funktion falsch ist.
- Geben Sie die entfernten Elemente mit `Array.prototype.slice()` zurück.
- Die `fn`-Callback-Funktion akzeptiert ein einzelnes Argument, das der Wert des Elements ist.

Verwenden Sie den folgenden Code, um die `takeWhile`-Funktion zu implementieren:

```js
const takeWhile = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (!fn(val)) return arr.slice(0, i);
  return arr;
};
```

Hier ist ein Beispiel für die Verwendung der `takeWhile`-Funktion, um Elemente aus einem Array basierend auf einer Bedingung zu entfernen:

```js
takeWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
