# Funktion zur Aufrundung einer Zeichenkette

Um eine Zeichenkette auf beiden Seiten mit dem angegebenen Zeichen aufzurunden, wenn sie kürzer als die angegebene `length` ist, verwenden Sie die folgende Funktion:

```js
const pad = (str, length, char = " ") =>
  str.padStart((str.length + length) / 2, char).padEnd(length, char);
```

Die Funktion verwendet `String.prototype.padStart()` und `String.prototype.padEnd()`, um beide Seiten der angegebenen Zeichenkette aufzurunden. Sie können das dritte Argument `char` weglassen, um das Leerzeichen als Standardauffüllzeichen zu verwenden.

Hier sind einige Beispiele für die Verwendung der `pad()`-Funktion:

```js
pad("cat", 8); // '  cat   '
pad(String(42), 6, "0"); // '004200'
pad("foobar", 3); // 'foobar'
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
