# 根据函数移除数组元素

要从数组中移除特定元素，请使用 `dropWhile` 函数，该函数会移除元素，直到传入的函数返回 `true`。然后，该函数会返回数组中剩余的元素。

其工作原理如下：

- 使用 `Array.prototype.slice()` 遍历数组，以删除数组的第一个元素，直到 `func` 返回的值为 `true`。
- 返回剩余的元素。

示例用法：

```js
const dropWhile = (arr, func) => {
  while (arr.length > 0 && !func(arr[0])) arr = arr.slice(1);
  return arr;
};

dropWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
