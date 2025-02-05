# 从数组中移除匹配的元素

要根据给定条件从数组中移除特定元素，你可以使用 `remove` 函数。该函数会通过移除给定函数返回 `false` 的元素来改变原始数组。

以下是使用 `remove` 函数的步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.filter()` 查找返回真值的数组元素。
3. 使用 `Array.prototype.reduce()` 通过 `Array.prototype.splice()` 移除元素。
4. 回调函数会被传入三个参数（值、索引、数组）。

```js
const remove = (arr, func) =>
  Array.isArray(arr)
    ? arr.filter(func).reduce((acc, val) => {
        arr.splice(arr.indexOf(val), 1);
        return acc.concat(val);
      }, [])
    : [];
```

以下是使用 `remove` 函数的示例：

```js
remove([1, 2, 3, 4], (n) => n % 2 === 0); // [2, 4]
```

这将返回一个包含已移除元素的新数组。
