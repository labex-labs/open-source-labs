# UUID in Browser generieren

Um in einem Browser eine UUID gemäß [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) Version 4 zu generieren, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein.
2. Verwenden Sie die Methode `Crypto.getRandomValues()`, um eine UUID zu generieren.
3. Konvertieren Sie die UUID in einen hexadezimalen String mithilfe der Methode `Number.prototype.toString()`.
4. Implementieren Sie folgenden Code:

```js
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
```

5. Rufen Sie die Funktion `UUIDGeneratorBrowser()` auf, um eine UUID zu generieren. Beispielsweise würde `UUIDGeneratorBrowser()` den Wert `'7982fcfe-5721-4632-bede-6000885be57d'` zurückgeben.
