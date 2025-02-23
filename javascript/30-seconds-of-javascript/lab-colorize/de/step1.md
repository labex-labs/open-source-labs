# Text färben

Um in der Konsole farbigen Text auszugeben, folgen Sie den folgenden Schritten und verwenden Sie die Funktion `colorize()`:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Verwenden Sie Template-Literale und spezielle Zeichen, um den passenden Farbcode zur Zeichenkettenergebnis hinzuzufügen.
- Um eine Hintergrundfarbe hinzuzufügen, fügen Sie am Ende der Zeichenkette ein spezielles Zeichen hinzu, das die Hintergrundfarbe zurücksetzt.

Die `colorize()`-Funktion erstellt ein Objekt mit 16 Eigenschaften, einschließlich der Farbcodes für Schwarz, Rot, Grün, Gelb, Blau, Magenta, Cyan und Weiß. Darüber hinaus hat sie Eigenschaften zum Hinzufügen einer Hintergrundfarbe zum Text.

Um die `colorize()`-Funktion zu verwenden, rufen Sie sie mit dem zu färbenden Text als Argument(en) auf, gefolgt von der Farb- oder Hintergrundfarbeigenschaft. Beispielsweise wird `colorize('foo').red` 'foo' mit roten Buchstaben ausgeben.

Verwenden Sie die `console.log()`-Funktion, um den farbigen Text in die Konsole auszugeben.

```js
const colorize = (...args) => ({
  black: `\x1b[30m${args.join(" ")}`,
  red: `\x1b[31m${args.join(" ")}`,
  green: `\x1b[32m${args.join(" ")}`,
  yellow: `\x1b[33m${args.join(" ")}`,
  blue: `\x1b[34m${args.join(" ")}`,
  magenta: `\x1b[35m${args.join(" ")}`,
  cyan: `\x1b[36m${args.join(" ")}`,
  white: `\x1b[37m${args.join(" ")}`,
  bgBlack: `\x1b[40m${args.join(" ")}\x1b[0m`,
  bgRed: `\x1b[41m${args.join(" ")}\x1b[0m`,
  bgGreen: `\x1b[42m${args.join(" ")}\x1b[0m`,
  bgYellow: `\x1b[43m${args.join(" ")}\x1b[0m`,
  bgBlue: `\x1b[44m${args.join(" ")}\x1b[0m`,
  bgMagenta: `\x1b[45m${args.join(" ")}\x1b[0m`,
  bgCyan: `\x1b[46m${args.join(" ")}\x1b[0m`,
  bgWhite: `\x1b[47m${args.join(" ")}\x1b[0m`
});
```

```js
console.log(colorize("foo").red); // 'foo' (rote Buchstaben)
console.log(colorize("foo", "bar").bgBlue); // 'foo bar' (blaue Hintergrund)
console.log(colorize(colorize("foo").yellow, colorize("foo").green).bgWhite);
// 'foo bar' (erstes Wort in gelben Buchstaben, zweites Wort in grünen Buchstaben, weißer Hintergrund für beide)
```
