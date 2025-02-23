# Funktion, um jedes n-te Element eines Arrays zurückzugeben

Um jedes `n-te` Element in einem Array zurückzugeben, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die Methode `Array.prototype.filter()`, um ein neues Array zu erstellen, das jedes `n-te` Element eines gegebenen Arrays enthält.
3. Verwenden Sie die folgende Funktion, um den obigen Schritt umzusetzen:

```js
const everyNth = (arr, nth) => arr.filter((e, i) => i % nth === nth - 1);
```

4. Um die Funktion zu testen, verwenden Sie folgenden Code:

```js
everyNth([1, 2, 3, 4, 5, 6], 2); // [ 2, 4, 6 ]
```

Dies wird ein neues Array mit jedem zweiten Element des Eingabearrays zurückgeben.
