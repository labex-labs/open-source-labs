# Eine Funktion zum Einrücken von Strings in JavaScript

Um jedem Zeile in einem angegebenen String Einrückungen hinzuzufügen, kannst du die `indentString()`-Funktion in JavaScript verwenden. Diese Funktion nimmt drei Argumente entgegen: `str`, `count` und `indent`.

- Das `str`-Argument stellt den String dar, den du einrücken möchtest.
- Das `count`-Argument bestimmt, wie oft du jede Zeile einrücken möchtest.
- Das `indent`-Argument ist optional und stellt das Zeichen dar, das du für die Einrückung verwenden möchtest. Wenn du es nicht angibst, ist der Standardwert ein einzelnes Leerzeichen (`' '`).

Hier ist der Code für die `indentString()`-Funktion:

```js
const indentString = (str, count, indent = " ") =>
  str.replace(/^/gm, indent.repeat(count));
```

Um diese Funktion zu verwenden, rufe einfach sie mit den gewünschten Argumenten auf. Hier sind einige Beispiele:

```js
indentString("Lorem\nIpsum", 2); // '  Lorem\n  Ipsum'
indentString("Lorem\nIpsum", 2, "_"); // '__Lorem\n__Ipsum'
```

Im ersten Beispiel gibt `indentString('Lorem\nIpsum', 2)` `'  Lorem\n  Ipsum'` zurück, was bedeutet, dass jede Zeile des Eingabe-Strings zweimal mit Leerzeichen eingerückt wurde.

Im zweiten Beispiel gibt `indentString('Lorem\nIpsum', 2, '_')` `'__Lorem\n__Ipsum'` zurück, was bedeutet, dass jede Zeile des Eingabe-Strings zweimal mit Unterstrich-Zeichen (`'_'`) eingerückt wurde.
