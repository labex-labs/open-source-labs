# 如何在 JavaScript 中使用递归深度扁平化数组

要在 JavaScript 中深度扁平化数组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用递归扁平化数组。
3. 将 `Array.prototype.concat()` 方法与空数组 (`[]`) 和展开运算符 (`...`) 一起使用来扁平化数组。
4. 递归地扁平化每个作为数组的元素。
5. 实现以下代码：

```js
const deepFlatten = (arr) =>
  [].concat(...arr.map((v) => (Array.isArray(v) ? deepFlatten(v) : v)));

deepFlatten([1, [2], [[3], 4], 5]); // [1, 2, 3, 4, 5]
```

通过遵循这些步骤，你可以轻松地在 JavaScript 中使用递归深度扁平化数组。
