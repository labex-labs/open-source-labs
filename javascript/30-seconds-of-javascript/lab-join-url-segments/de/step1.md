# URL-Segmente verknüpfen und normalisieren

Um gegebene URL-Segmente zusammenzufügen und die resultierende URL zu normalisieren, folgen Sie den Schritten unten:

1. Verwenden Sie `Array.prototype.join()`, um URL-Segmente zu kombinieren.
2. Verwenden Sie eine Reihe von `String.prototype.replace()`-Aufrufen mit verschiedenen regulären Ausdrücken, um die resultierende URL zu normalisieren, indem Sie:
   - Doppelte Schrägstriche entfernen
   - Die richtigen Schrägstriche für das Protokoll hinzufügen
   - Schrägstriche vor Parametern entfernen
   - Parameter mit `'&'` kombinieren und den ersten Parametertrenner normalisieren.

Verwenden Sie den folgenden Codeausschnitt, um URL-Segmente zu verknüpfen und zu normalisieren:

```js
const URLJoin = (...args) =>
  args
    .join("/")
    .replace(/[\/]+/g, "/")
    .replace(/^(.+):\//, "$1://")
    .replace(/^file:/, "file:/")
    .replace(/\/(\?|&|#[^!])/g, "$1")
    .replace(/\?/g, "&")
    .replace("&", "?");
```

Beispielverwendung:

```js
URLJoin("http://www.google.com", "a", "/b/cd", "?foo=123", "?bar=foo");
// 'http://www.google.com/a/b/cd?foo=123&bar=foo'
```
