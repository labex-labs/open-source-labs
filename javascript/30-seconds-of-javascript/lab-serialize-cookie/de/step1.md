# Wie man einen Cookie serialisiert

Um zu beginnen, das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Anschließend folgen Sie diesen Schritten, um ein Cookie-Name-Wert-Paar in einen Set-Cookie-Header-String zu serialisieren:

1. Verwenden Sie Template-Literale und `encodeURIComponent()`, um den passenden String zu erstellen.
2. Implementieren Sie die `serializeCookie`-Funktion, indem Sie die `name`- und `val`-Parameter übergeben.
3. Die Funktion wird einen richtig serialisierten String zurückgeben.

Hier ist ein Beispiel dafür, wie die `serializeCookie`-Funktion verwendet werden kann:

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

In diesem Beispiel nimmt die `serializeCookie`-Funktion `foo` als Cookie-Name und `bar` als Cookie-Wert entgegen und gibt einen serialisierten Cookie-String von `foo=bar` zurück.
