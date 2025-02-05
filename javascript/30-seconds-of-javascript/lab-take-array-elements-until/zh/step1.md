# 在满足条件之前移除数组元素

要在满足条件之前移除数组中的元素并获取被移除的元素，请按照以下步骤操作：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `for...of` 循环遍历 `Array.prototype.entries()` 返回的数组索引和元素对，直到作为参数传递的函数返回真值。
- 使用 `Array.prototype.slice()` 返回被移除的元素。
- 回调函数 `fn` 接受一个参数，即元素的值。

以下是一个示例代码片段：

```js
const takeUntil = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (fn(val)) return arr.slice(0, i);
  return arr;
};

takeUntil([1, 2, 3, 4], (n) => n >= 3); // [1, 2]
```

在上述示例中，`takeUntil()` 函数用于从 `[1, 2, 3, 4]` 数组中移除元素，直到元素的值大于或等于 3。输出结果为 `[1, 2]`。
