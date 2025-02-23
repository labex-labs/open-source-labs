# Überprüfen, ob ein Wert in JavaScript ein Symbol ist

Um zu überprüfen, ob ein Wert ein symbolisches Primitiv in JavaScript ist, kannst du den `typeof`-Operator verwenden. Hier ist ein Beispielcodeausschnitt, den du verwenden kannst:

```js
const isSymbol = (val) => typeof val === "symbol";
```

Du kannst die `isSymbol`-Funktion aufrufen und ein Symbol als Argument übergeben, um zu überprüfen, ob sie `true` zurückgibt. Hier ist ein Beispiel:

```js
isSymbol(Symbol("x")); // true
```
