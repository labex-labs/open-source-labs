# 如何将数组分组为对象

要将数组分组为对象，请执行以下步骤：

1. 打开终端或 SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.reduce()` 方法从这两个数组构建一个对象。
3. 提供一个有效的属性标识符数组和一个值数组。
4. 如果属性数组的长度比值数组长，其余的键将被设置为 `undefined`。
5. 如果值数组的长度比属性数组长，其余的值将被忽略。

以下是一个示例代码片段，展示了如何将数组分组为对象：

```js
const zipObject = (props, values) =>
  props.reduce((obj, prop, index) => ((obj[prop] = values[index]), obj), {});

zipObject(["a", "b", "c"], [1, 2]); // {a: 1, b: 2, c: undefined}
zipObject(["a", "b"], [1, 2, 3]); // {a: 1, b: 2}
```
