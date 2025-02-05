# 用于在数组中查找最接近数值匹配项的函数

要在数组中找到最接近的数字，请使用以下函数：

```js
const closest = (arr, n) =>
  arr.reduce((acc, num) => (Math.abs(num - n) < Math.abs(acc - n) ? num : acc));
```

以下是使用方法：

1. 打开终端/SSH。
2. 输入 `node`。
3. 使用 `closest()` 函数，并将数组和目标值作为参数提供。

示例用法：`closest([6, 1, 3, 7, 9], 5)` 将返回 `6`，它是数组中最接近 `5` 的数字。
