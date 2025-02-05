# 检查数组是否包含任何值

要开始练习编码，请打开终端/SSH并输入 `node`。

要检查一个数组是否至少包含另一个数组中的一个元素，请使用 `Array.prototype.some()` 和 `Array.prototype.includes()`。以下是一个示例函数：

```js
const includesAny = (arr, values) => values.some((v) => arr.includes(v));
```

你可以调用此函数，并传入要比较的两个数组作为参数。该函数将返回一个布尔值，指示 `values` 中的至少一个元素是否包含在 `arr` 中。以下是一些示例：

```js
includesAny([1, 2, 3, 4], [2, 9]); // true
includesAny([1, 2, 3, 4], [8, 9]); // false
```
