# 在JavaScript中创建冻结的Set对象

要在JavaScript中创建一个冻结的 `Set` 对象，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用 `Set` 构造函数从 `iterable` 创建一个新的 `Set` 对象。
3. 将新创建对象的 `add`、`delete` 和 `clear` 方法设置为 `undefined`，以有效地冻结该对象。

以下是一个示例代码片段：

```js
const frozenSet = (iterable) => {
  const s = new Set(iterable);
  s.add = undefined;
  s.delete = undefined;
  s.clear = undefined;
  return s;
};

console.log(frozenSet([1, 2, 3, 1, 2]));
// 输出：Set { 1, 2, 3, add: undefined, delete: undefined, clear: undefined }
```

这段代码从一个数字的可迭代对象创建一个冻结的 `Set` 对象，并返回其 `add`、`delete` 和 `clear` 方法设置为 `undefined` 的对象。
