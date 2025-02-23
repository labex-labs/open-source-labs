# Überprüfen, ob ein Wert null ist

Um zu überprüfen, ob ein Wert in JavaScript `null` ist, verwenden Sie den strikten Gleichheitsoperator (`===`). Hier ist ein Beispielcodeausschnitt, der eine Funktion namens `isNull` definiert, die `true` zurückgibt, wenn der gegebene Wert `null` ist, und `false` andernfalls.

```js
const isNull = (val) => val === null;
```

Um diese Funktion zu testen, können Sie sie mit dem Wert aufrufen, den Sie überprüfen möchten, als Argument. Beispielsweise wird `isNull(null)` `true` zurückgeben.
