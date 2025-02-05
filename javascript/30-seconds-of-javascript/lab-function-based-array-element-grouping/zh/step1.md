# 如何对数组元素进行分组

如果你想练习编码，可以先打开终端/SSH 并输入 `node`。准备好之后，你可以按照以下步骤根据给定函数对数组元素进行分组：

1. 使用 `Array.prototype.map()` 将数组的值映射到一个函数或属性名。
2. 使用 `Array.prototype.reduce()` 创建一个对象，其中的键由映射结果生成。

以下是一个示例代码片段：

```js
const groupBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val, i) => {
      acc[val] = (acc[val] || []).concat(arr[i]);
      return acc;
    }, {});
```

要测试这段代码，可以使用以下示例：

```js
groupBy([6.1, 4.2, 6.3], Math.floor); // {4: [4.2], 6: [6.1, 6.3]}
groupBy(["one", "two", "three"], "length"); // {3: ['one', 'two'], 5: ['three']}
```

这些将返回基于指定函数的键的对象，其值是与该函数匹配的原始元素的数组。
