# Wahrheitskontrollfunktion für eine Sammlung

Um zu üben, tippen Sie in der Konsole/SSH `node`.

Hier ist eine Funktion, die überprüft, ob eine Prädikatfunktion für alle Elemente einer Sammlung wahr ist.

- Verwenden Sie `Array.prototype.every()`, um zu überprüfen, ob jedes übergebene Objekt die angegebene Eigenschaft hat und ob es einen wahren Wert zurückgibt.

```js
const truthCheckCollection = (collection, pre) =>
  collection.every((obj) => obj[pre]);
```

Beispielverwendung:

```js
truthCheckCollection(
  [
    { user: "Tinky-Winky", sex: "male" },
    { user: "Dipsy", sex: "male" }
  ],
  "sex"
); // true
```
