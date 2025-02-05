# 如何序列化包含循环引用的 JSON

要序列化包含循环引用的 JSON 对象，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 创建一个 `WeakSet`，使用 `WeakSet.prototype.add()` 和 `WeakSet.prototype.has()` 来存储和检查已见过的值。
3. 将 `JSON.stringify()` 与一个自定义替换函数一起使用，该函数会忽略 `seen` 中已有的值，并在必要时添加新值。
4. ⚠️ **注意**：此函数会查找并删除循环引用，这会导致序列化的 JSON 中循环数据丢失。

以下是 `stringifyCircularJSON` 函数的代码：

```js
const stringifyCircularJSON = (obj) => {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (value !== null && typeof value === "object") {
      if (seen.has(value)) return;
      seen.add(value);
    }
    return value;
  });
};
```

要测试该函数，你可以创建一个具有循环引用的对象并调用 `stringifyCircularJSON`：

```js
const obj = { n: 42 };
obj.obj = obj;
stringifyCircularJSON(obj); // '{"n": 42}'
```
