# 根据函数从数组右侧删除元素

要从数组末尾删除元素，直到满足特定条件，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.slice()` 遍历数组，删除数组的最后一个元素，直到传入的 `func` 返回 `true`。
3. 返回数组中剩余的元素。

以下是一个示例实现：

```js
const dropRightWhile = (arr, func) => {
  let rightIndex = arr.length;
  while (rightIndex-- && !func(arr[rightIndex]));
  return arr.slice(0, rightIndex + 1);
};
```

你可以这样使用这个函数：

```js
dropRightWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
