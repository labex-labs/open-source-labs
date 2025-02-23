# Wie man in JavaScript einen Wert an einem bestimmten Index in einem Array einfügt

Um in JavaScript einen Wert an einem bestimmten Index in einem Array einzufügen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Array.prototype.splice()`-Methode mit einem geeigneten Index und einer Löschanzahl von `0`, indem Sie die anzugebenden einzufügenden Werte auffächern.
3. Die `insertAt`-Funktion nimmt ein Array, einen Index und einen oder mehrere Werte, die nach dem angegebenen Index eingefügt werden sollen.
4. Die Funktion mutiert das ursprüngliche Array und gibt das modifizierte Array zurück.

Hier ist ein Beispiel für die Funktion `insertAt` im Einsatz:

```js
const insertAt = (arr, i, ...v) => {
  arr.splice(i + 1, 0, ...v);
  return arr;
};

let myArray = [1, 2, 3, 4];
insertAt(myArray, 2, 5); // myArray = [1, 2, 3, 5, 4]

let otherArray = [2, 10];
insertAt(otherArray, 0, 4, 6, 8); // otherArray = [2, 4, 6, 8, 10]
```

Im obigen Beispiel wird die `insertAt`-Funktion verwendet, um den Wert `5` nach dem zweiten Index des `myArray`-Arrays einzufügen und die Werte `4`, `6` und `8` nach dem ersten Index des `otherArray`-Arrays einzufügen.
