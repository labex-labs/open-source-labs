# Wie man in JavaScript einen Wert maskiert

Um in JavaScript einen Wert zu maskieren, kannst du die `mask()`-Funktion verwenden. Folge diesen Schritten:

1. Öffne das Terminal/SSH und tippe `node`, um mit der Codeausführung zu beginnen.
2. Verwende `String.prototype.slice()`, um den Teil der Zeichen zu extrahieren, der nicht maskiert bleiben soll.
3. Verwende `String.prototype.padStart()`, um den Anfang der Zeichenfolge mit dem `mask`-Zeichen bis zur ursprünglichen Länge zu füllen.
4. Wenn du Zeichen am Ende der Zeichenfolge ausschließen möchtest, verwende einen negativen Wert für `num`.
5. Wenn du keinen Wert für `num` angibst, wird die Funktion standardmäßig die letzten 4 Zeichen unmaskiert lassen.
6. Wenn du keinen Wert für `mask` angibst, wird die Funktion standardmäßig das `'*'`-Zeichen für die Maskierung verwenden.

Hier ist der Code für die `mask()`-Funktion:

```js
const mask = (cc, num = 4, mask = "*") =>
  `${cc}`.slice(-num).padStart(`${cc}`.length, mask);
```

Und hier sind einige Beispiele dafür, wie die `mask()`-Funktion verwendet werden kann:

```js
mask(1234567890); // '******7890'
mask(1234567890, 3); // '*******890'
mask(1234567890, -4, "$"); // '$$$$567890'
```
