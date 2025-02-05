# 将对象转换为查询字符串

要将对象转换为查询字符串，请使用 `objectToQueryString()` 函数，该函数会根据给定对象的键值对生成查询字符串。

该函数的工作原理如下：

- 它在 `Object.entries()` 上使用 `Array.prototype.reduce()` 从 `queryParameters` 创建查询字符串。
- 它根据 `queryString` 的长度确定 `symbol` 是 `?` 还是 `&`。
- 仅当 `val` 是字符串时，才将其连接到 `queryString`。
- 当 `queryParameters` 为假值时，返回 `queryString` 或空字符串。

以下是 `objectToQueryString()` 函数的代码：

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

`objectToQueryString()` 函数的示例用法：

```js
objectToQueryString({ page: "1", size: "2kg", key: undefined }); // 返回 '?page=1&size=2kg'
```
