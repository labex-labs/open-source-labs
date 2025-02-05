# 如何在 JavaScript 中用符号表示对象键

要在 JavaScript 中用符号表示对象键，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Object.keys()` 方法获取要进行符号化的对象的键。
3. 使用 `Array.prototype.reduce()` 方法和 `Symbol` 创建一个新对象，其中每个键都转换为一个 `Symbol`。
4. 以下是一个示例代码片段：

```js
const symbolizeKeys = (obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({ ...acc, [Symbol(key)]: obj[key] }),
    {}
  );
```

5. 要测试该函数，请将你的对象作为参数调用 `symbolizeKeys()`，如下所示：

```js
symbolizeKeys({ id: 10, name: "apple" });
// { [Symbol(id)]: 10, [Symbol(name)]: 'apple' }
```

通过执行这些步骤，你可以轻松地在 JavaScript 中对任何对象的键进行符号化。
