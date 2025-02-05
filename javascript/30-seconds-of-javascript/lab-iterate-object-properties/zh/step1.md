# 如何在 JavaScript 中迭代对象自身的属性

要迭代对象自身的属性并进行编码练习，请按以下步骤操作：

1. 打开终端或 SSH。
2. 输入 `node` 以启动新的 Node.js 会话。
3. 使用 `Object.keys()` 方法获取对象自身属性的数组。
4. 使用 `Array.prototype.forEach()` 方法遍历每个属性并执行提供的函数。
5. 提供的函数应接受三个参数：属性值、属性键和对象本身。
6. 使用 `forOwn()` 函数和对象以及提供的函数来迭代对象的属性。

以下是一个示例代码片段：

```js
const forOwn = (obj, fn) =>
  Object.keys(obj).forEach((key) => fn(obj[key], key, obj));

forOwn({ foo: "bar", a: 1 }, (v) => console.log(v)); // 'bar', 1
```

这段代码会将 `foo` 和 `a` 属性的值输出到控制台。
