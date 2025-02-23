# Wie man in JavaScript Elemente in einem Array gruppiert und zählt

Um in JavaScript Elemente in einem Array zu gruppieren und zu zählen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die Methode `Array.prototype.map()`, um die Werte eines Arrays auf eine Funktion oder einen Eigenschaftsnamen abzubilden.
3. Verwenden Sie die Methode `Array.prototype.reduce()`, um ein Objekt zu erstellen, wobei die Schlüssel aus den abgebildeten Ergebnissen erzeugt werden.
4. Erstellen Sie eine Funktion namens `countBy`, die ein Array und eine Funktion als Argumente nimmt.
5. Innerhalb der `countBy`-Funktion verwenden Sie einen bedingten Operator, um zu überprüfen, ob das übergebene Argument eine Funktion oder ein Eigenschaftsname ist. Wenn es eine Funktion ist, verwenden Sie sie als die Abbildungsfunktion. Wenn es ein Eigenschaftsname ist, greifen Sie auf diese Eigenschaft der Arrayelemente zu.
6. Verwenden Sie die `reduce()`-Methode, um ein Objekt zu erstellen, wobei jeder Schlüssel ein einzigartiges Element im Array darstellt und dessen Wert die Anzahl der Vorkommen in dem Array ist.

Hier ist der Code:

```js
const countBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => {
      acc[val] = (acc[val] || 0) + 1;
      return acc;
    }, {});
```

Sie können die `countBy`-Funktion mit den folgenden Beispielen testen:

```js
countBy([6.1, 4.2, 6.3], Math.floor); // {4: 1, 6: 2}
countBy(["one", "two", "three"], "length"); // {3: 2, 5: 1}
countBy([{ count: 5 }, { count: 10 }, { count: 5 }], (x) => x.count); // {5: 2, 10: 1}
```
