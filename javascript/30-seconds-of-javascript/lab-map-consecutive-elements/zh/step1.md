# 用于映射数组中连续元素的函数

要开始编码，请打开终端/SSH 并输入 `node`。

此函数使用给定函数 `fn` 映射数组中每 `n` 个连续元素组成的块。请按以下步骤操作：

- 使用 `Array.prototype.slice()` 获取一个新数组 `arr`，其中移除了前 `n` 个元素。
- 使用 `Array.prototype.map()` 和 `Array.prototype.slice()` 将 `fn` 应用于 `arr` 中每 `n` 个连续元素组成的块。

以下是代码：

```js
const mapConsecutive = (arr, n, fn) =>
  arr.slice(n - 1).map((v, i) => fn(arr.slice(i, i + n)));
```

例如，你可以使用 `mapConsecutive()` 映射数字数组中每 3 个连续元素组成的块，并使用破折号连接它们：

```js
mapConsecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, (x) => x.join("-"));
// ['1-2-3', '2-3-4', '3-4-5', '4-5-6', '5-6-7', '6-7-8', '7-8-9', '8-9-10'];
```
