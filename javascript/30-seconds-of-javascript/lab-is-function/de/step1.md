# Überprüfen, ob ein Wert eine Funktion ist

Um zu überprüfen, ob ein Wert eine Funktion ist, können Sie den `typeof`-Operator mit dem `function`-Primitive verwenden.

Hier ist ein Beispiel für eine Funktion, die überprüft, ob ein bestimmter Wert eine Funktion ist:

```js
const isFunction = (val) => typeof val === "function";
```

Sie können es wie folgt verwenden:

```js
isFunction("x"); // false
isFunction((x) => x); // true
```

Um zu beginnen, mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
