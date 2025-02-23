# Eigenschaftsprüfer

Um zu überprüfen, ob eine bestimmte Eigenschaft eines Objekts einer bestimmten Bedingung entspricht, verwenden Sie die `checkProp`-Funktion. Diese Funktion erstellt eine gekürzte Funktion, die eine Prädikatsfunktion und einen Eigenschaftennamen als Argumente nimmt. Die zurückgegebene Funktion nimmt dann ein Objekt und gibt `true` oder `false` zurück, je nachdem, ob die angegebene Eigenschaft der von der Prädikatsfunktion angegebenen Bedingung entspricht.

Hier ist eine Beispielimplementierung von `checkProp`:

```js
const checkProp = (predicate, prop) => (obj) => !!predicate(obj[prop]);
```

Und hier sind einige Beispiele dafür, wie Sie sie verwenden könnten:

```js
const lengthIs4 = checkProp((l) => l === 4, "length");
lengthIs4([]); // false
lengthIs4([1, 2, 3, 4]); // true
lengthIs4(new Set([1, 2, 3, 4])); // false (Set verwendet Größe, nicht Länge)

const session = { user: {} };
const validUserSession = checkProp((u) => u.active && !u.disabled, "user");

validUserSession(session); // false

session.user.active = true;
validUserSession(session); // true

const noLength = checkProp((l) => l === undefined, "length");
noLength([]); // false
noLength({}); // true
noLength(new Set()); // true
```

Zusammenfassend lässt die `checkProp`-Funktion es Ihnen zu einfach überprüfen, den Wert einer bestimmten Eigenschaft eines Objekts, indem Sie eine Prädikatsfunktion für diese Eigenschaft angeben.
