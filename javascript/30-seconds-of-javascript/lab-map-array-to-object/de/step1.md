# Array in Objekt abbilden

Um die Werte eines Arrays mithilfe einer Funktion in ein Objekt abzubilden, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um die Code-Praxis zu starten.
2. Verwenden Sie `Array.prototype.reduce()`, um `fn` auf jedes Element in `arr` anzuwenden und die Ergebnisse zu einem Objekt zu kombinieren.
3. Verwenden Sie `el` als Schlüssel für jede Eigenschaft und das Ergebnis von `fn` als Wert.

Hier ist ein Beispiel-Codeausschnitt:

```js
const mapObject = (arr, fn) =>
  arr.reduce((acc, el, i) => {
    acc[el] = fn(el, i, arr);
    return acc;
  }, {});
```

Sie können die `mapObject`-Funktion wie in diesem Beispiel verwenden:

```js
mapObject([1, 2, 3], (a) => a * a); // { 1: 1, 2: 4, 3: 9 }
```
