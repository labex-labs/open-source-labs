# 不区分大小写的子字符串搜索

要检查一个字符串是否包含某个子字符串而不考虑其大小写，请按以下步骤操作：

- 使用带有 `'i'` 标志的 `RegExp` 构造函数创建一个正则表达式，该表达式匹配给定的 `searchString`，忽略大小写。
- 使用 `RegExp.prototype.test()` 检查字符串是否包含该子字符串。

以下是一个示例代码片段：

```js
const includesCaseInsensitive = (str, searchString) =>
  new RegExp(searchString, "i").test(str);
```

要测试此函数，可以运行：

```js
includesCaseInsensitive("Blue Whale", "blue"); // true
```
