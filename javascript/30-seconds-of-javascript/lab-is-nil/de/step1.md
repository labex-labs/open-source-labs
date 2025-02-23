# Wie man in JavaScript überprüft, ob ein Wert null oder undefined ist

Um zu bestimmen, ob ein Wert in JavaScript `null` oder `undefined` ist, kann man den strikten Gleichheitsoperator (`===`) verwenden. Hier ist ein Beispielcodeausschnitt, der überprüft, ob der angegebene Wert `null` oder `undefined` ist:

```js
const isNil = (val) => val === undefined || val === null;
```

Man kann diese Funktion verwenden, um zu überprüfen, ob ein Wert `null` oder `undefined` ist, wie folgt:

```js
isNil(null); // true
isNil(undefined); // true
isNil(""); // false
```

Um zu beginnen, JavaScript zu programmieren, kann man das Terminal/SSH öffnen und `node` eingeben.
