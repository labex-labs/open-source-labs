# Arrayelemente von rechts her entfernen

Um eine bestimmte Anzahl von Elementen von rechts eines Arrays zu entfernen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.slice()`, um die angegebene Anzahl von Elementen von rechts zu entfernen.
3. Wenn Sie nur ein Element entfernen möchten, können Sie das letzte Argument `n` weglassen, und der Standardwert `1` wird verwendet.

Hier ist ein Beispielcodeausschnitt:

```js
const dropRight = (arr, n = 1) => arr.slice(0, -n);
```

Sie können diese Funktion mit den folgenden Beispielen testen:

```js
dropRight([1, 2, 3]); // [1, 2]
dropRight([1, 2, 3], 2); // [1]
dropRight([1, 2, 3], 42); // []
```
