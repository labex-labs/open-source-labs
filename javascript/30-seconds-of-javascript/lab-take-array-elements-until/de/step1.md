# Entfernen von Array-Elementen bis eine Bedingung erfüllt ist

Um Elemente in einem Array bis eine Bedingung erfüllt ist zu entfernen und die entfernten Elemente zu erhalten, folgen Sie den Schritten unten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Iterieren Sie über das Array mithilfe einer `for...of`-Schleife über `Array.prototype.entries()`, bis die als Argument übergebene Funktion einen wahren Wert zurückgibt.
- Verwenden Sie `Array.prototype.slice()`, um die entfernten Elemente zurückzugeben.
- Die Callback-Funktion `fn` akzeptiert ein einzelnes Argument, das den Wert des Elements ist.

Hier ist ein Beispielcodeausschnitt:

```js
const takeUntil = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (fn(val)) return arr.slice(0, i);
  return arr;
};

takeUntil([1, 2, 3, 4], (n) => n >= 3); // [1, 2]
```

Im obigen Beispiel wird die `takeUntil()`-Funktion verwendet, um Elemente im Array `[1, 2, 3, 4]` bis der Wert größer oder gleich 3 ist zu entfernen. Die Ausgabe ist `[1, 2]`.
