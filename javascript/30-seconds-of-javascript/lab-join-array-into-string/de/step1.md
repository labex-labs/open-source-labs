# Wie man ein Array zu einem String zusammenführt

Um alle Elemente eines Arrays zu einem String zusammenzuführen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die Funktion `join()` mit den folgenden Parametern:
   - `arr`: das zu verbindende Array.
   - `separator` (optional): der Separator, der zwischen den Elementen des Arrays verwendet werden soll. Wenn nicht angegeben, wird der Standardseparator `,` verwendet.
   - `end` (optional): der Separator, der zwischen den letzten beiden Elementen des Arrays verwendet werden soll. Wenn nicht angegeben, wird der gleiche Wert wie `separator` standardmäßig verwendet.
3. Die `join()`-Funktion verwendet `Array.prototype.reduce()`, um die Elemente des Arrays zu einem String zu kombinieren.
4. Der endgültige String wird zurückgegeben.

Hier ist der Code für die `join()`-Funktion:

```js
const join = (arr, separator = ",", end = separator) =>
  arr.reduce(
    (acc, val, i) =>
      i === arr.length - 2
        ? acc + val + end
        : i === arr.length - 1
          ? acc + val
          : acc + val + separator,
    ""
  );
```

Und hier sind einige Beispiele für die Verwendung der `join()`-Funktion:

```js
join(["pen", "pineapple", "apple", "pen"], ",", "&"); // 'pen,pineapple,apple&pen'
join(["pen", "pineapple", "apple", "pen"], ","); // 'pen,pineapple,apple,pen'
join(["pen", "pineapple", "apple", "pen"]); // 'pen,pineapple,apple,pen'
```
