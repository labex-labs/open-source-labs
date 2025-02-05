# 将对象键转换为小写

要将对象的所有键转换为小写，请执行以下步骤：

1. 打开终端/SSH 开始练习编码并输入 `node`。
2. 使用 `Object.keys()` 获取对象键的数组。
3. 使用 `Array.prototype.reduce()` 将数组映射到一个对象。
4. 使用 `String.prototype.toLowerCase()` 将键转换为小写。

以下是实现这些步骤的示例代码：

```js
const lowerize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toLowerCase()] = obj[k];
    return acc;
  }, {});
```

然后，你可以将一个对象作为参数调用 `lowerize()` 函数，以获取一个所有键都为小写的新对象。例如：

```js
lowerize({ Name: "John", Age: 22 }); // { name: 'John', age: 22 }
```
