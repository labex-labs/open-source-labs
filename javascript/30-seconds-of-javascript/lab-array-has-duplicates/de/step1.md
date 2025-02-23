# Wie man auf Duplikate in einem Array überprüft

Um zu überprüfen, ob ein Array Duplikate enthält, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Set`, um die eindeutigen Werte im Array zu erhalten.
3. Verwenden Sie `Set.prototype.size` und `Array.prototype.length`, um zu überprüfen, ob die Anzahl der eindeutigen Werte der Anzahl der Elemente im ursprünglichen Array entspricht.

Hier ist ein Beispielcodeausschnitt, der auf Duplikate in einem Array überprüft:

```js
const hasDuplicates = (arr) => new Set(arr).size !== arr.length;
```

Sie können diese Funktion mit dem folgenden Code testen:

```js
hasDuplicates([0, 1, 1, 2]); // true
hasDuplicates([0, 1, 2, 3]); // false
```

Die `hasDuplicates`-Funktion gibt `true` zurück, wenn es in dem Array Duplikate gibt, und `false` andernfalls.
