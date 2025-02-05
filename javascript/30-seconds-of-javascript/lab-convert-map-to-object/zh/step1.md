# 在 JavaScript 中将 Map 转换为对象的说明

要将 JavaScript `Map` 转换为对象，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Map.prototype.entries()` 方法将 `Map` 转换为键值对数组。
3. 使用 `Object.fromEntries()` 方法将数组转换为对象。

以下是将 `Map` 转换为对象的示例代码片段：

```js
const mapToObject = (map) => Object.fromEntries(map.entries());
```

要测试该函数，你可以运行：

```js
mapToObject(
  new Map([
    ["a", 1],
    ["b", 2]
  ])
); // {a: 1, b: 2}
```
