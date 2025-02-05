# 以下是如何对数组中的每个元素反向执行函数

要从数组的最后一个元素开始，对每个数组元素执行一个函数，请执行以下步骤：

1. 使用 `Array.prototype.slice()` 克隆给定数组。
2. 使用 `Array.prototype.reverse()` 反转克隆后的数组。
3. 使用 `Array.prototype.forEach()` 遍历反转后的数组。

以下是一个示例代码片段：

```js
const forEachRight = (arr, callback) => arr.slice().reverse().forEach(callback);
```

你可以通过运行以下代码来测试该函数：

```js
forEachRight([1, 2, 3, 4], (val) => console.log(val)); // '4', '3', '2', '1'
```

要开始编码，请打开终端/SSH 并输入 `node`。
