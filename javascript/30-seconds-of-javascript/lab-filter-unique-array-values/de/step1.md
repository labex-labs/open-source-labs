# Wie man in JavaScript einzigartige Werte in einem Array filtert

Um in JavaScript einzigartige Werte in einem Array zu filtern, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den `Set`-Konstruktor und den Spread-Operator (`...`), um ein Array der einzigartigen Werte in Ihrem ursprünglichen Array zu erstellen.
3. Verwenden Sie `Array.prototype.filter()`, um ein Array zu erstellen, das nur die nicht-einzigartigen Werte enthält.
4. Definieren Sie eine Funktion namens `filterUnique`, die ein Array als Argument nimmt und die obigen Schritte darauf anwendet.
5. Rufen Sie die `filterUnique`-Funktion mit Ihrem Array als Argument auf.

Hier ist ein Beispielcodeausschnitt, um dies zu erreichen:

```js
const filterUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) !== arr.lastIndexOf(i));

filterUnique([1, 2, 2, 3, 4, 4, 5]); // [2, 4]
```

Im obigen Codeausschnitt nimmt die `filterUnique`-Funktion ein Array entgegen und wendet den `Set`-Konstruktor und die `Array.prototype.filter()`-Methode darauf an, um ein Array mit nur den nicht-einzigartigen Werten zurückzugeben.
