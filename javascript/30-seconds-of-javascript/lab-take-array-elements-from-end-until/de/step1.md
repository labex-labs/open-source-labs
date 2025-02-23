# Entfernen von Array-Elementen vom Ende, bis eine Bedingung erfüllt ist

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion entfernt Elemente vom Ende eines Arrays, bis die übergebene Funktion `true` zurückgibt, und gibt dann die entfernten Elemente zurück.

So funktioniert es:

- Erstellen Sie zunächst eine umgekehrte Kopie des Arrays mit dem Spread-Operator (`...`) und `Array.prototype.reverse()`.
- Gehen Sie anschließend mit einer `for...of`-Schleife über die umgekehrte Kopie von `Array.prototype.entries()` iterativ durch, bis der zurückgegebene Wert der Funktion wahr ist.
- Geben Sie danach die entfernten Elemente mit `Array.prototype.slice()` zurück.
- Die Callback-Funktion `fn` akzeptiert ein einzelnes Argument, das den Wert des Elements ist.

Hier ist der Code:

```js
const takeRightUntil = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

Hier ist ein Beispiel, wie diese Funktion verwendet werden kann:

```js
takeRightUntil([1, 2, 3, 4], (n) => n < 3); // [3, 4]
```
