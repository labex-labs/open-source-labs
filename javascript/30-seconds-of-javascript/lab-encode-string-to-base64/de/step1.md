# Ein String in Base64 codieren

Um ein String-Objekt in einen base-64 codierten ASCII-String zu codieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen zu programmieren.
2. Erstellen Sie einen `Buffer` mithilfe des gegebenen Strings und der binären Codierung.
3. Verwenden Sie `Buffer.prototype.toString()`, um den base-64 codierten String zurückzugeben.

Hier ist ein Beispielcodeausschnitt:

```js
const encodeToBase64 = (str) => Buffer.from(str, "binary").toString("base64");
```

Sie können jetzt die `encodeToBase64()`-Funktion verwenden, um jeden String in base-64 zu codieren. Beispiel:

```js
encodeToBase64("foobar"); // 'Zm9vYmFy'
```
