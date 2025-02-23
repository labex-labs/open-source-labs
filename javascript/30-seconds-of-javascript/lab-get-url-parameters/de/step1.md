# Objekt mit URL-Parametern

Um ein Objekt zu erstellen, das die Parameter der aktuellen URL enthält, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie `String.prototype.match()` mit einem passenden regulären Ausdruck, um alle Schlüssel-Wert-Paare zu extrahieren.
3. Verwenden Sie `Array.prototype.reduce()`, um sie in ein einzelnes Objekt zuzuordnen und zu kombinieren.
4. Geben Sie `location.search` als Argument, um es auf die aktuelle URL anzuwenden.

Hier ist der Code:

```js
const getURLParameters = (url) =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => (
      (a[v.slice(0, v.indexOf("="))] = v.slice(v.indexOf("=") + 1)), a
    ),
    {}
  );
```

Sie können diese Funktion mit jeder URL verwenden, um ein Objekt mit ihren Parametern zu erhalten. Hier sind einige Beispiele:

```js
getURLParameters("google.com"); // {}
getURLParameters("http://url.com/page?name=Adam&surname=Smith");
// {name: 'Adam','surname': 'Smith'}
```
