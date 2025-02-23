# オブジェクトをクエリ文字列に変換する

オブジェクトをクエリ文字列に変換するには、`objectToQueryString()` 関数を使用します。この関数は、与えられたオブジェクトのキーと値のペアからクエリ文字列を生成します。

この関数の動作は以下の通りです。

- `Object.entries()` の `Array.prototype.reduce()` を使用して、`queryParameters` からクエリ文字列を作成します。
- `queryString` の長さに基づいて、`symbol` を `?` または `&` に設定します。
- `val` が文字列の場合のみ、`queryString` に連結します。
- `queryParameters` が偽の値の場合、`queryString` または空文字列を返します。

以下は、`objectToQueryString()` 関数のコードです。

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

`objectToQueryString()` 関数の使用例です。

```js
objectToQueryString({ page: "1", size: "2kg", key: undefined }); // returns '?page=1&size=2kg'
```
