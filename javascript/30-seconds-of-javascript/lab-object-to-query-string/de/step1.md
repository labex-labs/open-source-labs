# Umwandlung eines Objekts in eine Abfragezeichenfolge

Um ein Objekt in eine Abfragezeichenfolge umzuwandeln, verwenden Sie die Funktion `objectToQueryString()`, die aus den Schlüssel-Wert-Paaren des angegebenen Objekts eine Abfragezeichenfolge generiert.

Die Funktion funktioniert wie folgt:

- Sie verwendet `Array.prototype.reduce()` auf `Object.entries()`, um die Abfragezeichenfolge aus `queryParameters` zu erstellen.
- Sie bestimmt das `Symbol` als entweder `?` oder `&` basierend auf der Länge von `queryString`.
- Sie konkateniert `val` nur dann an `queryString`, wenn es sich um einen String handelt.
- Sie gibt die `queryString` oder einen leeren String zurück, wenn `queryParameters` falsch ist.

Hier ist der Code für die Funktion `objectToQueryString()`:

```js
const objectToQueryString = (queryParameters) => {
  return queryParameters
    ? Object.entries(queryParameters).reduce(
        (queryString, [key, val], index) => {
          const symbol = queryString.length === 0 ? "?" : "&";
          queryString +=
            typeof val === "string" ? `${symbol}${key}=${val}` : "";
          return queryString;
        },
        ""
      )
    : "";
};
```

Beispielverwendung der Funktion `objectToQueryString()`:

```js
objectToQueryString({ page: "1", size: "2kg", key: undefined }); // gibt '?page=1&size=2kg' zurück
```
