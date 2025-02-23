# Überprüfen, ob ein Wert ein Boolean ist

Um zu überprüfen, ob ein Wert ein boolescher primitiver Wert in JavaScript ist, verwenden Sie den `typeof`-Operator mit dem `===`-Vergleichsoperator.

```js
const isBoolean = (val) => typeof val === "boolean";
```

Hier ist ein Beispiel dafür, wie die `isBoolean()`-Funktion verwendet wird, um zu überprüfen, ob ein Wert ein Boolean ist:

```js
isBoolean(null); // gibt false zurück
isBoolean(false); // gibt true zurück
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
