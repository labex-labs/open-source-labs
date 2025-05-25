# Convertendo um Objeto para uma _Query String_

Para converter um objeto em uma _query string_, use a função `objectToQueryString()`, que gera uma _query string_ a partir dos pares chave-valor do objeto fornecido.

A função funciona da seguinte forma:

- Ela usa `Array.prototype.reduce()` em `Object.entries()` para criar a _query string_ a partir de `queryParameters`.
- Ela determina o `symbol` a ser `?` ou `&` com base no comprimento de `queryString`.
- Ela concatena `val` a `queryString` somente se for uma _string_.
- Ela retorna a `queryString` ou uma _string_ vazia quando `queryParameters` é _falsy_.

Aqui está o código para a função `objectToQueryString()`:

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

Exemplo de uso da função `objectToQueryString()`:

```js
objectToQueryString({ page: "1", size: "2kg", key: undefined }); // returns '?page=1&size=2kg'
```
