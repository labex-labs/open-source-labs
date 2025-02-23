# Umwandeln einer Abfragezeichenfolge in ein Objekt

Um eine Abfragezeichenfolge oder eine URL in ein Objekt umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `String.prototype.split()`, um die Parameter aus der angegebenen `url` zu extrahieren.
3. Verwenden Sie den `URLSearchParams`-Konstruktor, um ein Objekt zu erstellen und es mit dem Spread-Operator (`...`) in ein Array von Schlüssel-Wert-Paaren zu konvertieren.
4. Verwenden Sie `Array.prototype.reduce()`, um das Array von Schlüssel-Wert-Paaren in ein Objekt umzuwandeln.

Hier ist der Code, um die Abfragezeichenfolge umzuwandeln:

```js
const queryStringToObject = (url) =>
  [...new URLSearchParams(url.split("?")[1])].reduce(
    (a, [k, v]) => ((a[k] = v), a),
    {}
  );
```

Beispielverwendung:

```js
queryStringToObject("https://google.com?page=1&count=10");
// {page: '1', count: '10'}
```
