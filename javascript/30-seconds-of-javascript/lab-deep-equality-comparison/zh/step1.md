# 如何在 JavaScript 中检查对象相等性

要检查两个值是否相等，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `equals()` 函数对两个值进行深度比较。
3. 检查两个值是否相同。如果是，则返回 `true`。
4. 使用 `Date.prototype.getTime()` 检查两个值是否都是具有相同时间的 `Date` 对象。如果是，则返回 `true`。
5. 检查两个值是否为具有相等值的非对象值（严格比较）。如果是，则返回 `true`。
6. 检查是否只有一个值为 `null` 或 `undefined`，或者它们的原型是否不同。如果是，则返回 `false`。
7. 如果上述条件都不满足，则使用 `Object.keys()` 检查两个值是否具有相同数量的键。
8. 使用 `Array.prototype.every()` 检查 `a` 中的每个键是否存在于 `b` 中，并且通过递归调用 `equals()` 检查它们是否相等。

使用以下代码实现 `equals()` 函数：

```js
const equals = (a, b) => {
  if (a === b) return true;

  if (a instanceof Date && b instanceof Date)
    return a.getTime() === b.getTime();

  if (!a || !b || (typeof a !== "object" && typeof b !== "object"))
    return a === b;

  if (a.prototype !== b.prototype) return false;

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every((k) => equals(a[k], b[k]));
};
```

使用以下代码示例测试 `equals()` 函数：

```js
equals(
  { a: [2, { e: 3 }], b: [4], c: "foo" },
  { a: [2, { e: 3 }], b: [4], c: "foo" }
); // true

equals([1, 2, 3], { 0: 1, 1: 2, 2: 3 }); // true
```
