# Verwendung von Argument-Zusammenfassung

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Argument-Zusammenfassung ist eine Technik, die verwendet wird, um das erste definierte, nicht-null-Argument in einer Liste von Argumenten zurückzugeben. Um dies zu erreichen, verwenden Sie `Array.prototype.find()` und `Array.prototype.includes()`, um den ersten Wert zu finden, der nicht gleich `undefined` oder `null` ist.

Hier ist ein Beispiel dafür, wie Argument-Zusammenfassung in JavaScript verwendet wird:

```js
const coalesce = (...args) => args.find((v) => ![undefined, null].includes(v));
```

In der obigen Codeausschnitt ist `coalesce` eine Funktion, die beliebig viele Argumente annimmt und das erste definierte, nicht-null-Argument zurückgibt. Hier ist ein Beispiel dafür, wie die `coalesce`-Funktion verwendet wird:

```js
coalesce(null, undefined, "", NaN, "Waldo"); // ''
```

In diesem Beispiel wird `coalesce` mit einer Liste von Argumenten aufgerufen, die `null`, `undefined`, eine leere Zeichenfolge `''`, `NaN` und die Zeichenfolge `'Waldo'` enthält. Die Funktion gibt eine leere Zeichenfolge `''` zurück, da es das erste definierte, nicht-null-Argument in der Liste ist.
