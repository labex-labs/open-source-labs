# 数组排名

要进行编码练习，请打开终端/SSH 并输入`node`。此函数根据比较函数计算数组的排名。

要使用此函数，你可以：

- 使用`Array.prototype.map()`和`Array.prototype.filter()`，通过提供的比较函数将每个元素映射到一个排名。

以下是一个示例用法：

```js
const ranking = (arr, compFn) =>
  arr.map((a) => arr.filter((b) => compFn(a, b)).length + 1);
```

示例：

```js
ranking([8, 6, 9, 5], (a, b) => a < b);
// [2, 3, 1, 4]
ranking(["c", "a", "b", "d"], (a, b) => a.localeCompare(b) > 0);
// [3, 1, 2, 4]
```
