# Convertir un objeto a una cadena de consulta

Para convertir un objeto en una cadena de consulta, utiliza la función `objectToQueryString()` que genera una cadena de consulta a partir de los pares clave-valor del objeto dado.

La función funciona de la siguiente manera:

- Utiliza `Array.prototype.reduce()` en `Object.entries()` para crear la cadena de consulta a partir de `queryParameters`.
- Determina el `símbolo` que puede ser `?` o `&` en función de la longitud de `queryString`.
- Concatena `val` a `queryString` solo si es una cadena.
- Devuelve la `queryString` o una cadena vacía cuando los `queryParameters` son falsos.

Aquí está el código de la función `objectToQueryString()`:

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

Uso de ejemplo de la función `objectToQueryString()`:

```js
objectToQueryString({ page: "1", size: "2kg", key: undefined }); // devuelve '?page=1&size=2kg'
```
