# Überprüfen, ob ein Wert in JavaScript eine Zahl ist

Um zu überprüfen, ob ein Wert in JavaScript eine Zahl ist, können Sie den `typeof`-Operator verwenden, um zu bestimmen, ob der Wert als numerisches primitiver Typ klassifiziert wird. Um Probleme mit `NaN` zu vermeiden, das einen `typeof`-Wert von `number` hat und nicht gleich sich selbst ist, können Sie auch überprüfen, ob der Wert mit `val === val` gleich sich selbst ist.

Hier ist eine Beispiel-Funktion, die überprüft, ob ein gegebener Wert eine Zahl ist:

```js
const isNumber = (val) => typeof val === "number" && val === val;
```

Sie können diese Funktion wie folgt verwenden:

```js
isNumber(1); // true
isNumber("1"); // false
isNumber(NaN); // false
```
