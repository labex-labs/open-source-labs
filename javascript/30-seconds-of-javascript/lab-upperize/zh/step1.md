# 如何在 JavaScript 中将对象的键转换为大写

要在 JavaScript 中将对象的所有键转换为大写，请执行以下步骤：

1. 使用 `Object.keys()` 获取对象键的数组。
2. 使用 `Array.prototype.reduce()` 将数组映射到一个对象。
3. 使用 `String.prototype.toUpperCase()` 将键转换为大写。

以下是代码：

```js
const upperize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toUpperCase()] = obj[k];
    return acc;
  }, {});
```

要测试该函数，你可以这样调用它：

```js
upperize({ Name: "John", Age: 22 }); // { NAME: 'John', AGE: 22 }
```
