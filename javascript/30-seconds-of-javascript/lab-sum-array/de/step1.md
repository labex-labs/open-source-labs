# So finden Sie die Summe eines Arrays

Um die Summe eines Arrays von Zahlen zu finden, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen zu programmieren.
2. Verwenden Sie die `Array.prototype.reduce()`-Methode, um jeden Wert einem Akkumulator hinzuzufügen, der mit einem Wert von `0` initialisiert werden sollte.
3. Hier ist der Code, den Sie verwenden können, um die Summe des Arrays zu finden:

```js
const sum = (...arr) => [...arr].reduce((acc, val) => acc + val, 0);
```

4. Um die `sum`-Funktion zu testen, verwenden Sie die folgenden Codebeispiele:

```js
sum(1, 2, 3, 4); // 10
sum(...[1, 2, 3, 4]); // 10
```

Indem Sie diese Schritte befolgen, können Sie mit JavaScript leicht die Summe eines Arrays von Zahlen finden.
