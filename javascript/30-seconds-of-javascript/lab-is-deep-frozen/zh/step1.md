# 如何检查一个对象是否被深度冻结

要检查一个对象是否被深度冻结，请在JavaScript中按以下步骤操作：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用递归检查对象的所有属性是否都被深度冻结。
3. 对给定对象使用 `Object.isFrozen()` 检查它是否被浅冻结。
4. 使用 `Object.keys()` 获取对象的所有属性，并使用 `Array.prototype.every()` 检查所有键是否都是深度冻结的对象或非对象值。

以下是一个检查对象是否被深度冻结的示例代码片段：

```js
const isDeepFrozen = (obj) =>
  Object.isFrozen(obj) &&
  Object.keys(obj).every(
    (prop) => typeof obj[prop] !== "object" || isDeepFrozen(obj[prop])
  );
```

你可以使用 `isDeepFrozen` 函数像这样检查一个对象是否被深度冻结：

```js
const x = Object.freeze({ a: 1 });
const y = Object.freeze({ b: { c: 2 } });
isDeepFrozen(x); // true
isDeepFrozen(y); // false
```
