# Funktion zum Überprüfen von Ja/Nein-Zeichenfolgen

Um zu überprüfen, ob eine Zeichenfolge eine „ja“- oder „nein“-Antwort ist, verwenden Sie die folgende Funktion im Terminal/SSH, indem Sie `node` eingeben:

```js
const yesNo = (val, def = false) =>
  /^(y|yes)$/i.test(val) ? true : /^(n|no)$/i.test(val) ? false : def;
```

- Die Funktion gibt `true` zurück, wenn die Zeichenfolge `'y'`/`'yes'` ist, und `false`, wenn die Zeichenfolge `'n'`/`'no'` ist.
- Um eine Standardantwort festzulegen, lassen Sie das zweite Argument `def` weg. Standardmäßig wird die Funktion `false` zurückgeben.
- Die Funktion verwendet `RegExp.prototype.test()`, um zu überprüfen, ob die Zeichenfolge mit `'y'`/`'yes'` oder `'n'`/`'no'` übereinstimmt.

Beispielverwendung:

```js
yesNo("Y"); // true
yesNo("yes"); // true
yesNo("No"); // false
yesNo("Foo", true); // true
```
