# Bytes in einen menschenlesbaren String umwandeln

Um eine Zahl in Bytes in einen menschenlesbaren String umzuwandeln, verwenden Sie die Funktion `prettyBytes()`. Hier sind einige Dinge, die Sie beachten sollten:

- Die Funktion verwendet ein Array-Wörterbuch von Einheiten, das basierend auf dem Exponenten zugegriffen werden kann.
- Sie können das zweite Argument, `precision`, verwenden, um die Zahl auf eine bestimmte Anzahl von Stellen zu kürzen. Der Standardwert ist `3`.
- Sie können das dritte Argument, `addSpace`, verwenden, um einen Leerraum zwischen der Zahl und der Einheit hinzuzufügen. Der Standardwert ist `true`.
- Die Funktion gibt den aufgeräumten String zurück, indem sie ihn aufbaut, wobei die angegebenen Optionen und ob die Zahl negativ ist oder nicht berücksichtigt werden.

Hier ist der Code für die Funktion `prettyBytes()`:

```js
const prettyBytes = (num, precision = 3, addSpace = true) => {
  const UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  if (Math.abs(num) < 1) return num + (addSpace ? " " : "") + UNITS[0];
  const exponent = Math.min(
    Math.floor(Math.log10(num < 0 ? -num : num) / 3),
    UNITS.length - 1
  );
  const n = Number(
    ((num < 0 ? -num : num) / 1000 ** exponent).toPrecision(precision)
  );
  return (num < 0 ? "-" : "") + n + (addSpace ? " " : "") + UNITS[exponent];
};
```

Und hier sind einige Beispiele für die Verwendung der Funktion `prettyBytes()`:

```js
prettyBytes(1000); // '1 KB'
prettyBytes(-27145424323.5821, 5); // '-27.145 GB'
prettyBytes(123456789, 3, false); // '123MB'
```
