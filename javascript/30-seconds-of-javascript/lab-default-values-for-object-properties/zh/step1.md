# 如何为对象属性设置默认值

要为对象中所有 `undefined` 的属性设置默认值，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Object.assign()` 创建一个新的空对象，并复制原始对象以保持键顺序。
3. 使用 `Array.prototype.reverse()` 和展开运算符 (`...`) 从左到右组合默认值。
4. 最后，再次使用 `obj` 覆盖最初有值的属性。

以下是一个代码片段示例：

```js
const defaults = (obj, ...defs) =>
  Object.assign({}, obj, ...defs.reverse(), obj);

defaults({ a: 1 }, { b: 2 }, { b: 6 }, { a: 3 }); // { a: 1, b: 2 }
```

此代码片段将返回一个对象，该对象为原始对象中所有未定义的属性设置了默认值。
