# Wie man in JavaScript passende Array-Elemente herausfiltert

Um Elemente in einem JavaScript-Array herauszufiltern, die einen oder mehrere bestimmten Werte haben, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal oder SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.
2. Verwenden Sie die `Array.prototype.includes()`-Methode, um die auszuschließenden Werte zu finden.
3. Verwenden Sie die `Array.prototype.filter()`-Methode, um ein neues Array mit den ausgeschlossenen Elementen zu erstellen.

Hier ist ein Beispielcodeausschnitt:

```js
const without = (arr, ...args) => arr.filter((v) => !args.includes(v));

without([2, 1, 2, 3], 1, 2); // [3]
```

In diesem Beispiel nimmt die `without`-Funktion ein Array `arr` und ein oder mehrere Argumente `args` entgegen. Die Funktion verwendet die `filter()`-Methode, um ein neues Array zu erstellen, das alle Elemente ausschließt, die mit einem der in `args` angegebenen Werte übereinstimmen. Die `includes()`-Methode wird verwendet, um zu überprüfen, ob der Wert in `args` enthalten ist. Schließlich gibt die Funktion das neue Array mit den ausgeschlossenen Elementen zurück.
