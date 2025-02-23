# Wie man ein Objekt in JavaScript tief einfriert

Um ein Objekt in JavaScript tief einzufrieren, folge diesen Schritten:

1. Verwende `Object.keys()`, um alle Eigenschaften des übergebenen Objekts zu erhalten.
2. Iteriere über die Eigenschaften mit `Array.prototype.forEach()`.
3. Rufe `Object.freeze()` rekursiv auf alle Eigenschaften, die Objekte sind, und wende `deepFreeze()` erforderlichenfalls an.
4. Schließlich verwende `Object.freeze()`, um das gegebene Objekt einzufrieren.

Hier ist der Code:

```js
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};
```

Du kannst das tief eingefrorene Objekt mit dem folgenden Code testen:

```js
"use strict";

const val = deepFreeze([1, [2, 3]]);

val[0] = 3; // nicht erlaubt
val[1][0] = 4; // ebenfalls nicht erlaubt
```

Der obige Code wird einen Fehler werfen, da das `val`-Objekt tief eingefroren ist und nicht geändert werden kann.
