# 检查字符串是否为有效的 JSON

要检查给定的字符串是否为有效的 JSON，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `JSON.parse()` 方法和 `try...catch` 块来检查提供的字符串是否为有效的 JSON。
3. 如果字符串有效，则返回 `true`。否则，返回 `false`。

以下是实现此逻辑的示例代码片段：

```js
const isValidJSON = (str) => {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
};
```

你可以使用不同的输入字符串测试此函数，如下所示：

```js
isValidJSON('{"name":"Adam","age":20}'); // true
isValidJSON('{"name":"Adam",age:"20"}'); // false
isValidJSON(null); // false
```

在最后一个示例中，`null` 不是有效的 JSON 字符串，因此函数返回 `false`。
