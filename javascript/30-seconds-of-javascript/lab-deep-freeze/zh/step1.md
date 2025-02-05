# 如何在JavaScript中深度冻结对象

要在JavaScript中深度冻结一个对象，请遵循以下步骤：

1. 使用 `Object.keys()` 获取传入对象的所有属性。
2. 使用 `Array.prototype.forEach()` 遍历这些属性。
3. 对所有是对象的属性递归调用 `Object.freeze()`，必要时应用 `deepFreeze()`。
4. 最后，使用 `Object.freeze()` 冻结给定的对象。

以下是代码：

```js
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};
```

你可以使用以下代码测试深度冻结的对象：

```js
"use strict";

const val = deepFreeze([1, [2, 3]]);

val[0] = 3; // 不允许
val[1][0] = 4; // 同样不允许
```

上述代码将抛出一个错误，因为 `val` 对象被深度冻结，无法修改。
