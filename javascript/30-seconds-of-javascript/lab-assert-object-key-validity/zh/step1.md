# 验证对象键

要确保对象中的所有键都与指定的 `keys` 匹配，请执行以下步骤：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `Object.keys()` 获取对象 `obj` 的键。
- 使用 `Array.prototype.every()` 和 `Array.prototype.includes()` 来验证对象中的每个键是否包含在 `keys` 数组中。

以下是一个示例实现：

```js
const validateObjectKeys = (obj, keys) =>
  Object.keys(obj).every((key) => keys.includes(key));
```

你可以像这样使用该函数：

```js
validateObjectKeys({ id: 10, name: "apple" }, ["id", "name"]); // true
validateObjectKeys({ id: 10, name: "apple" }, ["id", "type"]); // false
```
