# Entfernen von Array-Elementen vom Ende, bis eine Bedingung erfüllt ist

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist eine Funktion, die Elemente vom Ende eines Arrays entfernt, bis die übergebene Funktion `false` zurückgibt. Anschließend werden die entfernten Elemente zurückgegeben.

Um sie zu verwenden, erstellen Sie eine umgekehrte Kopie des Arrays mit dem Spread-Operator (`...`) und `Array.prototype.reverse()`. Anschließend durchlaufen Sie die umgekehrte Kopie mit einer `for...of`-Schleife über `Array.prototype.entries()`, bis der zurückgegebene Wert der Funktion falsch ist.

Die Callback-Funktion `fn` akzeptiert ein einzelnes Argument, das den Wert des Elements ist. Am Ende geben Sie die entfernten Elemente mit `Array.prototype.slice()` zurück.

```js
const takeRightWhile = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (!fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

Hier ist ein Beispiel, wie die Funktion verwendet werden kann:

```js
takeRightWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```
