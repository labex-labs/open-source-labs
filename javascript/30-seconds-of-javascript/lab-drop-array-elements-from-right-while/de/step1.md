# Entfernen von Array-Elementen von rechts basierend auf einer Funktion

Um Elemente vom Ende eines Arrays bis zu einer bestimmten Bedingung entfernt zu werden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Iterieren Sie über das Array mithilfe von `Array.prototype.slice()`, um das letzte Element des Arrays zu entfernen, bis die übergebene `func` `true` zurückgibt.
3. Geben Sie die verbleibenden Elemente im Array zurück.

Hier ist eine Beispielimplementierung:

```js
const dropRightWhile = (arr, func) => {
  let rightIndex = arr.length;
  while (rightIndex-- && !func(arr[rightIndex]));
  return arr.slice(0, rightIndex + 1);
};
```

Sie können diese Funktion wie folgt verwenden:

```js
dropRightWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
