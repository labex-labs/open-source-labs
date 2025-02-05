# 如何在 JSON 对象中获取嵌套值

要根据给定的键从嵌套的 JSON 对象中检索目标值，请执行以下步骤：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `in` 运算符检查 `obj` 中是否存在 `target`。
- 如果找到 `target`，则返回 `obj` 中相应的值。
- 如果未找到 `target`，则使用 `Object.values()` 和 `Array.prototype.reduce()` 对每个嵌套对象递归调用 `dig` 函数，直到找到第一个匹配的键/值对。

以下是 `dig` 函数的代码：

```js
const dig = (obj, target) =>
  target in obj
    ? obj[target]
    : Object.values(obj).reduce((acc, val) => {
        if (acc !== undefined) return acc;
        if (typeof val === "object") return dig(val, target);
      }, undefined);
```

要使用 `dig` 函数，首先创建一个具有嵌套层级的 JSON 对象，如下所示：

```js
const data = {
  level1: {
    level2: {
      level3: "some data"
    }
  }
};
```

然后，使用 JSON 对象和所需的键调用 `dig` 函数：

```js
dig(data, "level3"); //'some data'
dig(data, "level4"); // undefined
```

这些示例将返回 `data` 对象中 `level3` 键的值，对于不存在的 `level4` 键则返回 `undefined`。
