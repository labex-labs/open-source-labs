# JavaScript-Funktion zum Analysieren von HTTP-Cookies

Um einen HTTP-Cookie-Header-Zeichenfolge in JavaScript zu analysieren und ein Objekt aller Cookie-Name-Wert-Paare zurückzugeben, folgen Sie diesen Schritten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
- Verwenden Sie `String.prototype.split()`, um Schlüssel-Wert-Paare voneinander zu trennen.
- Verwenden Sie `Array.prototype.map()` und `String.prototype.split()`, um Schlüssel von Werten in jedem Paar zu trennen.
- Verwenden Sie `Array.prototype.reduce()` und `decodeURIComponent()`, um ein Objekt mit allen Schlüssel-Wert-Paaren zu erstellen.

Hier ist ein Beispiel für die `parseCookie()`-Funktion, die die obigen Schritte implementiert:

```js
const parseCookie = (str) =>
  str
    .split(";")
    .map((v) => v.split("="))
    .reduce((acc, v) => {
      acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
      return acc;
    }, {});
```

Sie können die Funktion wie folgt testen:

```js
parseCookie("foo=bar; equation=E%3Dmc%5E2");
// { foo: 'bar', equation: 'E=mc^2' }
```
