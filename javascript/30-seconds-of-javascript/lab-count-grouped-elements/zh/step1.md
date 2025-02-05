# 如何使用 JavaScript 对数组中的元素进行分组和计数

要使用 JavaScript 对数组中的元素进行分组和计数，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.map()` 方法将数组的值映射到函数或属性名称。
3. 使用 `Array.prototype.reduce()` 方法创建一个对象，其中键由映射结果生成。
4. 创建一个名为 `countBy` 的函数，该函数接受一个数组和一个函数作为参数。
5. 在 `countBy` 函数内部，使用三元运算符检查传递的参数是函数还是属性名称。如果是函数，则将其用作映射函数。如果是属性名称，则访问数组元素的该属性。
6. 使用 `reduce()` 方法创建一个对象，其中每个键代表数组中的一个唯一元素，其值是它在数组中出现的次数。

以下是代码：

```js
const countBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => {
      acc[val] = (acc[val] || 0) + 1;
      return acc;
    }, {});
```

你可以使用以下示例测试 `countBy` 函数：

```js
countBy([6.1, 4.2, 6.3], Math.floor); // {4: 1, 6: 2}
countBy(["one", "two", "three"], "length"); // {3: 2, 5: 1}
countBy([{ count: 5 }, { count: 10 }, { count: 5 }], (x) => x.count); // {5: 2, 10: 1}
```
