# Wie man ein Element in einem Array umschaltet

Um ein Element in einem Array umzuschalten, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Überprüfen Sie, ob das gegebene Element im Array vorhanden ist, indem Sie `Array.prototype.includes()` verwenden.
3. Wenn das Element im Array vorhanden ist, verwenden Sie `Array.prototype.filter()`, um es zu entfernen.
4. Wenn das Element nicht im Array vorhanden ist, verwenden Sie den Spread-Operator (`...`), um es hinzuzufügen.
5. Verwenden Sie die `toggleElement`-Funktion, die ein Array und einen Wert akzeptiert, um das Element im Array umzuschalten.

```js
const toggleElement = (arr, val) =>
  arr.includes(val) ? arr.filter((el) => el !== val) : [...arr, val];

toggleElement([1, 2, 3], 2); // [1, 3]
toggleElement([1, 2, 3], 4); // [1, 2, 3, 4]
```

Indem Sie diese Schritte befolgen, können Sie mit JavaScript leicht ein Element in einem Array umschalten.
