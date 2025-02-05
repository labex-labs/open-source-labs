# 在JavaScript中截断字符串

要在JavaScript中截断字符串，你可以使用 `truncateString` 函数。该函数接受两个参数：`str`（要截断的字符串）和 `num`（截断后字符串的最大长度）。

`truncateString` 函数会检查 `str` 的长度是否大于 `num`。如果是，函数会将字符串截断到所需长度，并在末尾追加 `'...'`。如果不是，则返回原始字符串。

以下是 `truncateString` 函数的代码：

```js
const truncateString = (str, num) =>
  str.length > num ? str.slice(0, num > 3 ? num - 3 : num) + "..." : str;
```

以下是使用 `truncateString` 函数的示例：

```js
truncateString("boomerang", 7); // 'boom...'
```
